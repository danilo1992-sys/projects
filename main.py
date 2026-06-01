from InquirerPy import prompt
from comands.astro import astro
from comands.vite import vite
from comands.uv import uv_submenu
from comands.angular import angular
from comands.rspack import rspcak


def main():

    opciones = {
        "Astro": astro,
        "Vite": vite,
        "UV": uv_submenu,
        "Angular": angular,
        "Rspack": rspcak,
    }

    while True:
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
        opcion = result["opcion"]

        if opcion == "Salir":
            break

        if opcion in opciones:
            opciones[opcion]()
        else:
            print(f"[!] Opcion '{opcion}' no implementada aun")


if __name__ == "__main__":
    main()
