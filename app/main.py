from google import genai
from dotenv import load_dotenv
import os
import json

from tools.tool_registry import TOOLS

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def load_agent_context():
    with open("AGENTS.md", "r") as f:
        return f.read()


def build_prompt(state):
    context = load_agent_context()
    prompt = f"""
You are an AI agent.

Available tools:

1. add_task
2. list_tasks

You may use multiple tools if needed.

IMPORTANT:
Return ONLY valid JSON.
If the user request has already been completed,
you MUST return:

{{
  "final_answer": "task completed",
  "done": true
}}

Do NOT repeat actions that were already completed.


Possible formats:

To use a tool:
{{
  "action": "tool_name",
  "input": "tool input",
  "done": false
}}

When task is complete:
{{
  "final_answer": "your response",
  "done": true
}}

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
    tool_input = action_data["input"]

    if action not in TOOLS:
        result = f"Unknown action: {action}"
    else:
        tool_function = TOOLS[action]
        result = tool_function(tool_input) if tool_input else tool_function()

    state["tool_history"].append(
    {
        "tool": action,
        "input": tool_input,
        "result": result
    }
)

    return result


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
                model="gemini-3-flash-preview",
                contents=prompt
            )

            raw_response = response.text.strip()

            print(f"\nModel output:\n{raw_response}\n")

            try:
                action_data = json.loads(raw_response)

                if action_data.get("done"):

                    print(
                        f"\nFinal Answer:\n{action_data['final_answer']}\n"
                    )

                    break

                result = execute_action(action_data, state)

                print(f"\nTool Result:\n{result}\n")

            except Exception as e:
                print(f"\nError:\n{e}\n")
                break
if __name__ == "__main__":
    main()