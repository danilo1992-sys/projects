from comands.utils import ejecutar_comandos, folder
from InquirerPy import prompt
from main import main


def vite():
    ejecutar_comandos("npm create vite@latest")

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
        ejecutar_comandos("npm install tailwindcss @tailwindcss/vite")
        main()
        print(
            "Deve configurar la inatlacion https://tailwindcss.com/docs/installation/using-vite"
        )
    else:
        main()
        print("Volviendo al menu principal")
