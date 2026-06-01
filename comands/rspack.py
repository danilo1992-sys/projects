from comands.utils import ejecutar_comandos, folder
from InquirerPy import prompt


def rspcak():
    ejecutar_comandos("npm create rsbuild@latest")
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
        ejecutar_comandos(
            "npm install tailwindcss @tailwindcss/postcss postcss postcss-loader"
        )
        print(
            "Deve configurar la instalacion https://tailwindcss.com/docs/installation/framework-guides/rspack/react"
        )
