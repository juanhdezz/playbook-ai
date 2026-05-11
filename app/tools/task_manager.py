import json
from pathlib import Path

TASKS_FILE = Path("data/tasks.json")

def load_tasks():
    if TASKS_FILE.exists():
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)

    return f"Task '{task}' added successfully."

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    return "/n".join([f"- {task}" for task in tasks])

