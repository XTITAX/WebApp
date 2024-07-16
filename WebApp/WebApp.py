import subprocess
import webbrowser

def WebSite(filepath, folderpath):
    # Запускаем веб-сервер с помощью subprocess
    subprocess.run([r"jdk-22\bin\jwebserver.exe", "-d", folderpath], shell=True)

    # Формируем URL для открытия веб-страницы
    url = f"http://127.0.0.1:8000/{filepath}"

    # Открываем URL в браузере
    webbrowser.open_new(url)
