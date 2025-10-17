
import time
import pyautogui
import pyperclip
from decorators.executa_dia_util import executar_dia_util


def enviar_mensagem(contato, tema=''):
    try:  
        tema.low() 
        if tema == 'relatorio':
            pyautogui.click(496, 260)#clica na barra de pesquisa
            time.sleep(1)
            
            # Digitar nome do contato
            pyperclip.copy(contato["Nome"])
            pyautogui.hotkey("ctrl", "v")
            time.sleep(0.5)
            pyautogui.press('enter')
            time.sleep(1)
            
            # Pressiona Enter para abrir a conversa
            pyautogui.click(979, 971)
            time.sleep(1)
            
            # Digita a mensagem
            #pyautogui.click()
            pyperclip.copy(contato["mensagem"])
            pyautogui.hotkey("ctrl", "v")
            time.sleep(0.5)
            
            # Envia
            pyautogui.press("enter")
            time.sleep(1)
        elif tema == 'financeiro':
            pyautogui.click(496, 260)#clica na barra de pesquisa
            time.sleep(1)
            
            # Digitar nome do contato
            pyperclip.copy(contato["Nome"])
            pyautogui.hotkey("ctrl", "v")
            time.sleep(0.5)
            pyautogui.press('enter')
            time.sleep(1)
            
            # Pressiona Enter para abrir a conversa
            pyautogui.click(979, 971)
            time.sleep(1)
            
            # Digita a mensagem
            #pyautogui.click()
            pyperclip.copy(contato["mensagem"])
            pyautogui.hotkey("ctrl", "v")
            time.sleep(0.5)
            
            # Envia
            pyautogui.press("enter")
            time.sleep(1)
        elif tema == 'comercial':
            pyautogui.click(496, 260)#clica na barra de pesquisa
            time.sleep(1)
            
            # Digitar nome do contato
            pyperclip.copy(contato["Nome"])
            pyautogui.hotkey("ctrl", "v")
            time.sleep(0.5)
            pyautogui.press('enter')
            time.sleep(1)
            
            # Pressiona Enter para abrir a conversa
            pyautogui.click(979, 971)
            time.sleep(1)
            
            # Digita a mensagem
            #pyautogui.click()
            pyperclip.copy(contato["mensagem"])
            pyautogui.hotkey("ctrl", "v")
            time.sleep(0.5)
            
            # Envia
            pyautogui.press("enter")
            time.sleep(1)
        else:
            print(f"Tema '{tema}' não reconhecido. Mensagem não enviada para {contato['Nome']}.")
    except Exception as e:
            print(f"Erro ao enviar mensagem para {contato['nome']}: {e}")
    