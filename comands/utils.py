import subprocess
import os


def folder(ruta):
    os.chdir(ruta)


def ejecutar_comandos(cmd):
    subprocess.run(cmd, shell=True)
