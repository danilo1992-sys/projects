from InquirerPy import prompt
from comands.astro import astro


def main():
    menu = [
        {
            "type": "list",
            "message": "Creador de proyectos de Nodejs, Python y Go",
            "choices": [
                "Astro",
                "Svelte",
                "Angular",
                "UV",
                "Rspack",
                "Flowbite",
                "Go",
                "Bun",
                "Salir",
            ],
            "name": "opcion",
        }
    ]
    result = prompt(menu)

    if result["opcion"] == "Astro":
        astro()


if __name__ == "__main__":
    main()
