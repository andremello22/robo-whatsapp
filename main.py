# -*- coding: utf-8 -*-

from funcoes.enviar_mensagem import enviar_mensagem
from daddos.dados import  WHATSAPP_PATH, formata_planilha
from funcoes.abrir_whatsapp import abrir_whatsapp
from gui.caixa_de_selecao import CaixaDeSelecao


if __name__ == "__main__":
    caixaDeSelecao = CaixaDeSelecao()
    selecionado = caixaDeSelecao.resultado
    
    contatos = formata_planilha()
    abrir_whatsapp(WHATSAPP_PATH)




    for contato in contatos:
        enviar_mensagem(selecionado, contato)
 