from InquirerPy import prompt
import os


def create_archive(name):
    if not name.lower().endswith(".sh"):
        return f"{name}.sh"
    return name


def bash():
    questions = [
        {
            "type": "input",
            "message": "ingrese el nombre del script",
            "name": "script",
        }
    ]
    result = prompt(questions)
    script_path = create_archive(result["script"])
    script_content = "#!/usr/bin/env bash\n\n"
    try:
        with open(script_path, "w") as f:
            f.write(script_content)

        os.chmod(script_path, 0o755)
        print("[*] Archivo creado con exito")
    except Exception:
        print("[!] Error al crear el script")
