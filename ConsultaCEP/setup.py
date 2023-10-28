import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os"], "includes": ["flet", "time", "requests"], "include_files": ["./assets/fonts/Roboto-Regular.ttf","./assets/images/logo.png", "./assets/images/favicon.ico"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Consulta CEP Python",
    version="1.0",
    description="Buscador de CEPS em Python",
    options={"build_exe": build_exe_options},
    executables=[Executable(script="app.py", base=base, icon="./assets/images/favicon.icon")]
)