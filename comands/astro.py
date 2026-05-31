from comands.utils import ejecutar_comandos, folder
from InquirerPy import prompt


def astro():
    ejecutar_comandos("npm create astro@latest")
    instalar = [
        {
            "type": "input",
            "message": "Ingrese el nombre de la carpeta",
            "name": "folder",
        },
        {
            "type": "confirm",
            "message": "Desea instalar Tailwindcss",
            "name": "tailwind",
            "default": True,
        },
        {
            "type": "confirm",
            "message": "Desea instalar node como adaptador",
            "name": "node",
            "default": True,
        },
    ]
    result = prompt(instalar)
    folder(result["folder"])
    if result["tailwind"]:
        ejecutar_comandos("npx astro add tailwind")
    if result["node"]:
        ejecutar_comandos("npx astro add node")
