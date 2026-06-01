from InquirerPy import prompt
from comands.astro import astro
from comands.vite import vite


def main():
    menu = [
        {
            "type": "list",
            "message": "Creador de proyectos de Nodejs, Python y Go",
            "choices": [
                "Astro",
                "Vite",
                "Angular",
                "UV",
                "Rspack",
                "Flowbite",
                "Go",
                "Bun",
                "Bash",
                "Salir",
            ],
            "name": "opcion",
        }
    ]
    result = prompt(menu)

    if result["opcion"] == "Astro":
        astro()
    elif result["opcion"] == "Vite"


if __name__ == "__main__":
    main()
