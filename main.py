from funcoes.enviar_mensagem import enviar_mensagem
from daddos.dados import contatos, WHATSAPP_PATH
from funcoes.abrir_whatsapp import abrir_whatsapp

if __name__ == "__main__":
    abrir_whatsapp(WHATSAPP_PATH)

    for contato in contatos:
        enviar_mensagem(contato)
 