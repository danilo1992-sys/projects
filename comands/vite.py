from comands.utils import spinner, folder
from InquirerPy import prompt


def vite():
    spinner("npm create vite@latest")

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

    if result["tailwind"]:
        spinner("npm install tailwindcss @tailwindcss/vite")
        print(
            "Deve configurar la instalacion https://tailwindcss.com/docs/installation/using-vite"
        )
    else:
        print("Volviendo al menu principal")
