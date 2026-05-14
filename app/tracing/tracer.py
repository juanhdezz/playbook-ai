import json
from pathlib import Path
from datetime import datetime


TRACE_FILE = Path("tracing/agent_traces.jsonl") # jsonl es un fromato de archivo que almacena objetos JSON separados por saltos de línea, lo que facilita la lectura y escritura de grandes cantidades de datos estructurados.


def save_trace(trace_data):

    trace_data["timestamp"] = datetime.now().isoformat()

    with open(TRACE_FILE, "a") as f:

        f.write(json.dumps(trace_data) + "\n")