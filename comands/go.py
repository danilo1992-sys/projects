from InquirerPy import prompt
from comands.utils import folder, spinner, comprobar, shell_config
import requests
import os
import sys


def go_download():
    url = "https://go.dev/VERSION?m=text"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text.strip().splitlines()[0]
    except Exception:
        print("[!] Error al obtener la version de go")
        sys.exit(1)


def go():
    if not comprobar("go"):
        print("[!] go no esta instalado en el sistema")
        version = go_download()
        filename = f"{version}.linux-amd64.tar.gz"
        download = f"https://go.dev/dl/{filename}"
        spinner(f"wget {download}")
        spinner("sudo rm -rf /usr/local/go")
        spinner(f"sudo tar -C /usr/local -xzf {filename}")
        os.remove(filename)
        shell_config()
    else:
        print("[*] go ya esta instalado")

    instalar = [
        {
            "type": "input",
            "message": "Ingrese el nombre de la carpeta",
            "name": "folder",
            "validate": lambda x: len(x) > 0 or "El nombre del proyecto esta vacio",
        },
    ]

    result = prompt(instalar)
    name = result["folder"]
    os.mkdir(name)
    folder(name)
    spinner("go mod init main")
