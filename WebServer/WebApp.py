import subprocess
import webbrowser

def WebSite(path):
    subprocess.run(["@echo", "off"], shell=True)
    subprocess.run(["jdk-22\bin\jwebserver.exe"], shell=True)
    webbrowser.open_new("http://127.0.0.1:8000" + path)
WebSite("/index.html")