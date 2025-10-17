from interface_func.nome_func import FUNCOES
from daddos.dados import formata_planilha


def enviar_mensagem(nome_funcao: str, *args, **kwargs):
    func =  FUNCOES.get(nome_funcao)
    if func:
        return func(*args, **kwargs)
    else:
        raise ValueError(f"Função '{nome_funcao}' não encontrada.")
        return None 
contatos = formata_planilha()

  
       
    