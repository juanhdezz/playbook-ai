from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Load agent context from AGENTS.md, so the agent can understand its role and the project details. This file should contain information about the agent's purpose, capabilities, and any specific guidelines for behavior.
def load_agent_context():
    with open("AGENTS.md", "r") as f:
        return f.read()


def build_prompt(user_input):
    context = load_agent_context()

    prompt = f"""
You are a personal AI agent designed to help with daily planning, productivity, and sports.

Use the following project context to guide your behavior:

{context}

User request:
{user_input}

Your task:
- Provide a clear and structured plan for the day
- Balance work, study, and training
- Be practical and realistic

Output format:
- Morning
- Afternoon
- Evening
- Notes

Be concise. Avoid generic advice. Focus on actionable steps.
"""

    return prompt


def main():
    print("⚽ Playbook AI - Daily Planner (type 'exit' to quit)\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        prompt = build_prompt(user_input)

        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=prompt
        )

        print(f"\nAI:\n{response.text}\n")


if __name__ == "__main__":
    main()