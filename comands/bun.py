from comands.utils import spinner, comprobar, folder
from InquirerPy import prompt
import os


def bun():
    if not comprobar("bun"):
        print("[!] bun no esta instalado en el sistema")
        spinner("npm install -g bun")
    else:
        print("[*] bun ya esta instalado")

    instalar = [
        {
            "type": "input",
            "message": "Ingrese el nombre de la carpeta",
            "name": "folder",
        },
    ]
    result = prompt(instalar)
    os.mkdir(result["folder"])
    folder(result["folder"])
    spinner(f"bun init {result['folder']}")
