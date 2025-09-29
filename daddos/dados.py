from openpyxl import load_workbook

def formata_planilha():
    try:

        caminho = 'C:\\Users\\supor\\Documents\\boot-mfprint\\daddos\\planilha\\Contatos.xlsx'
        wb = load_workbook(caminho)
        ws = wb.active

        headers = [cell.value for cell in ws[1]]

        contatos = []
        for row in ws.iter_rows(min_row=2, values_only=True):  # começa da linha 2
            contato = dict(zip(headers, row))
            contato['Nome'] = contato['Nome'].strip()  # Remove espaços em branco extras
            contatos.append(contato)

        return contatos
    except Exception as e:
        print(f"Erro ao formatar planilha: {e}")
   



WHATSAPP_PATH = {"url":"https://web.whatsapp.com/",   "chrome_path":"C:/Program Files/Google/Chrome/Application/chrome.exe %s"}



