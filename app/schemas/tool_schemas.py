from pydantic import BaseModel,Field
# Con esto estams formalizando la entrada d elos datos
# para cada tool, asegurandonos de que el LLM devuelve las respuestas en el formato correcto, 
# nos sirve de guardrail para que el runtime no falle, y ademas nos ayuda a documentar claramente que se espera de cada herramienta,
# lo que es especialmente útil a medida que el número de herramientas crece y se vuelve más difícil recordar los detalles de cada una.

# Define una estructura de datos (usando la librería Pydantic) que exige que, para añadir una tarea, 
# el sistema debe proporcionar obligatoriamente un texto llamado task_name

class AddTaskInput(BaseModel):
    task_name: str = Field(description="Nombre de la tarea")


class ListTasksInput(BaseModel):
    pass