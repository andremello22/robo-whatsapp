
import time
import pyautogui


def enviar_mensagem(contato):
      # Abrir busca do WhatsApp (atalho CTRL+F)
    pyautogui.click(212, 250)
    time.sleep(1)
    
    # Digitar nome do contato
    pyautogui.typewrite(contato["nome"])
    pyautogui.press('enter')
    time.sleep(1.5)
    
    # Pressiona Enter para abrir a conversa
    pyautogui.click(226, 488)
    time.sleep(1)
    
    # Digita a mensagem
    #pyautogui.click()
    pyautogui.typewrite(contato["mensagem"])
    time.sleep(0.5)
    
    # Envia
    pyautogui.press("enter")
    time.sleep(1)
   