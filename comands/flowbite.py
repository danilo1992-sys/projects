from comands.utils import spinner, folder
from InquirerPy import prompt


def flowbite():
    instlar = [
        {
            "type": "input",
            "message": "Ingrese el nombre de la carpeta",
            "name": "folder",
        },
    ]

    result = prompt(instlar)
    spinner(f"npx create-flowbite-react@latest {result['folder']}")
