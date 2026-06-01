from InquirerPy import prompt

from comands.utils import spinner


def uv_submenu():
    preguntas = [
        {
            "type": "input",
            "message": "Ingrese el nombre del proyecto",
            "name": "name",
            "validate": lambda x: len(x) > 0 or "El nombre del proyecto esta vacio",
        }
    ]
    result = prompt(preguntas)
    name = result["name"]
    spinner(f"uv init {name}")
