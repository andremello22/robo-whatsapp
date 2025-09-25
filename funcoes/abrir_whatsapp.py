import webbrowser
import time
from decorators.executa_dia_util import executar_dia_util

@executar_dia_util(dia=1)
def abrir_whatsapp(dados):
    webbrowser.get(dados['chrome_path']).open(dados['url'])
    time.sleep(15)

