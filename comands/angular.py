from comands.utils import spinner, comprobar, folder
from InquirerPy import prompt


def angular():
    if not comprobar("ng"):
        print("[!] ng no esta instalado en el sistema")
        spinner("npm install -g @angular/cli")
    else:
        print("[*] ng ya esta instalado")

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
    ]
    result = prompt(instalar)
    folder(result["folder"])
    spinner(f"ng new {result['folder']}")

    if result["tailwind"]:
        spinner(f"cd {result['folder']} && ng add @tailwindcss/postcss")
