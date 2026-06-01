import subprocess
import os
from halo import Halo


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
    with Halo(text='instalando...', spinner='dots'):
        ejecutar_comandos(cmd)
