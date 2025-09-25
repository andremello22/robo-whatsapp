from openpyxl import Workbook

def gera_xlsx():
    wb = Workbook()
    ws = wb.active
    ws.title = "Contatos"

    ws.append(["Nome", "mensagem"])
    caminho = 'C:\\Users\\supor\\Documents\\boot-mfprint\\daddos\\planilha\\Contatos.xlsx'
    wb.save(caminho)

    return True


gera_xlsx()