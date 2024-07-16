import subprocess
import webbrowser

def WebSite(filepath, folderpath):
    subprocess.run(["@echo", "off"], shell=True)
    subprocess.run([f"jdk-22\\bin\\jwebserver.exe -d {folderpath}"], shell=True)
    webbrowser.open_new("http://127.0.0.1:8000" + filepath)
