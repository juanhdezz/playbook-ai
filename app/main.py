import json
import os

from dotenv import load_dotenv
from google import genai
from tools.tool_registry import TOOLS

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def load_agent_context():
    with open("AGENTS.md", "r") as f:
        return f.read()


import json


def build_prompt(state):
    context = load_agent_context()
    tools_description = generate_tools_prompt()

    # Hemos duplicado las llaves en las secciones de JSON de ejemplo
    prompt = f"""
You are an AI agent.

Available tools:

{tools_description}

You may use multiple tools if needed.

IMPORTANT:
Return ONLY valid JSON.
If the user request has already been completed,
you MUST return:

{{{{
  "final_answer": "task completed",
  "done": true
}}}}

Do NOT repeat actions that were already completed.


Possible formats:

To use a tool:
{{{{
  "action": "add_task",
  "parameters": {{
        "task_name": "Go to gym"
  }},
  "done": false
}}}}

When task is complete:
{{{{
  "final_answer": "your response",
  "done": true
}}}}

Current state:

User request:
{state["user_request"]}

Tool history:
{json.dumps(state["tool_history"], indent=2)}

Context:
{context}
"""
    return prompt


def execute_action(action_data, state):

    action = action_data["action"]

    parameters = action_data.get("parameters", {})

    if action not in TOOLS:
        result = f"Unknown action: {action}"

    else:

        tool_data = TOOLS[action]

        tool_function = tool_data["function"]

        schema = tool_data["schema"]

        validated_input = schema(**parameters)

        result = tool_function(**validated_input.model_dump())

    state["tool_history"].append({
        "tool": action,
        "parameters": parameters,
        "result": result
    })

    return result


# Esto añade autoamticamente al prompt las tools disponibles que tenemos y su descripcion y configuracion, ganamos escalabilidad
def generate_tools_prompt():
    tools_text = ""

    for tool_name, tool_data in TOOLS.items():
        tools_text += f"""
Tool: {tool_name}
Description: {tool_data["description"]}
Parameters:
"""

        for param_name, param_data in tool_data["parameters"].items():
            tools_text += f"""
- {param_name} ({param_data["type"]}):
  {param_data["description"]}
"""

    return tools_text


def create_initial_state(user_input):
    return {"user_request": user_input, "tool_history": [], "done": False}


def main():
    print("⚽ Playbook AI Agent Loop\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        state = create_initial_state(user_input)

        max_iterations = 5

        for iteration in range(max_iterations):
            print(f"\n--- Iteration {iteration + 1} ---")

            prompt = build_prompt(state)

            response = client.models.generate_content(
                model="gemini-3-flash-preview", contents=prompt
            )

            raw_response = response.text.strip()

            print(f"\nModel output:\n{raw_response}\n")

            try:
                action_data = json.loads(raw_response)

                if action_data.get("done"):
                    print(f"\nFinal Answer:\n{action_data['final_answer']}\n")

                    break

                result = execute_action(action_data, state)

                print(f"\nTool Result:\n{result}\n")

            except Exception as e:
                print(f"\nError:\n{e}\n")
                break


if __name__ == "__main__":
    main()
