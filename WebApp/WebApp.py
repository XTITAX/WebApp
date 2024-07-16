import subprocess
import webbrowser

def WebSite(filepath, folderpath):
    # Запускаем веб-сервер с помощью subprocess
    subprocess.run(["jwebserver", "-d", folderpath], shell=True)

    # Открываем URL в браузере
    webbrowser.open_new(f"http://127.0.0.1:8000/{filepath}")
