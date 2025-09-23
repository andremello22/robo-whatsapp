import webbrowser
import time


def abrir_whatsapp(dados):
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    url = "https://web.whatsapp.com/"
    webbrowser.get(dados['chrome_path']).open(dados['url'])
    time.sleep(20)

