from tools.task_manager import add_task, list_tasks
from schemas.tool_schemas import AddTaskInput, ListTasksInput

# Define the available tools and their corresponding functions.
# Interface define the available tools and their corresponding functions.

TOOLS = {
    "add_task": {
        "function": add_task,
        "description": "Add a new task to the task list",
        "parameters": {
            "task_name": {
                "type": "string",
                "description": "The task to add",
            }  # Aquí se define el parámetro que se espera para la función add_task, en este caso es un string llamado task_name, con su descripción correspondiente
        },
        "schema" : AddTaskInput
        
    },
    "list_tasks": {
        "function": list_tasks,
        "description": "List all existing tasks",
        "parameters": {},
    },
    "schema" : ListTasksInput
}
