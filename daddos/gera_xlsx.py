from openpyxl import Workbook
import os
def gera_xlsx(nome_arquivo='contatos'):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    CAMINHO_PLANILHAS = os.path.join(BASE_DIR, 'planilha', f'{nome_arquivo}.xlsx')
    CAMINHO_PLANILHAS = os.path.normpath(CAMINHO_PLANILHAS)


    wb = Workbook()
    ws = wb.active
    ws.title = "Contatos"

    ws.append(["Nome", "mensagem", "mensagem2"])
    caminho = CAMINHO_PLANILHAS
    wb.save(caminho)

    return True


gera_xlsx('relatorios')
gera_xlsx('financeiro')