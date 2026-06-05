import subprocess
import os
from halo import Halo
import pathlib


def shell_config():
    shell = os.environ.get("SHELL", "")
    home = pathlib.Path.home()
    go_path = 'export PATH="$PATH:/usr/local/go/bin"'

    if "zsh" in shell:
        config_file = home / ".zshrc"
    elif "bash" in shell:
        config_file = home / ".bashrc"
    elif "fish" in shell:
        config_file = home / ".config" / "fish" / "config.fish"
        go_path = "set -gx PATH $PATH /usr/local/go/bin"
    else:
        config_file = home / ".bashrc"

    if config_file.exists():
        content = config_file.read_text()
        if "/usr/local/go/bin" not in content:
            with open(config_file, "a") as f:
                f.write(f"\n{go_path}\n")
            print(f"[*] PATH de Go agregado en {config_file}")
    else:
        with open(config_file, "w") as f:
            f.write(f"{go_path}\n")
        print(f"[*] Archivo {config_file} creado con PATH de Go")


def comprobar(programa):
    try:
        subprocess.run([programa, "--version"], capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def folder(ruta):
    os.chdir(ruta)


def ejecutar_comandos(cmd):
    subprocess.run(cmd, shell=True)


def spinner(cmd):
    with Halo(text="instalando...", spinner="dots"):
        ejecutar_comandos(cmd)
