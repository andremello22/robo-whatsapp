
import time
import pyautogui
import pyperclip
from decorators.executa_dia_util import executar_dia_util

@executar_dia_util(dia=1)
def enviar_mensagem(contato):
    try:   
        # Abrir busca do WhatsApp (atalho CTRL+F)
        pyautogui.click(212, 250)#clica na barra de pesquisa
        time.sleep(1)
        
        # Digitar nome do contato
        pyautogui.write(contato["nome"])
        pyautogui.press('enter')
        time.sleep(1.5)
        
        # Pressiona Enter para abrir a conversa
        pyautogui.click(226, 488)
        time.sleep(1)
        
        # Digita a mensagem
        #pyautogui.click()
        pyperclip.copy(contato["mensagem"])
        pyautogui.hotkey("ctrl", "v")
        time.sleep(0.5)
        
        # Envia
        pyautogui.press("enter")
        time.sleep(1)
    except Exception as e:
        print(f"Erro ao enviar mensagem para {contato['nome']}: {e}")
    