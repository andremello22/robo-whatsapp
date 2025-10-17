import tkinter as tk

class CaixaDeSelecao:
    def __init__(self):
        self.opcoes = [
            "enviar_relatorio",
            "enviar_financeiro"
        ]
        self.resultado = None

        # Agora armazenamos como atributos da instância
        self.root = tk.Tk()
        self.root.title("Seleção de Função")
        self.root.geometry("300x200")

        self.opcao_var = tk.StringVar(value="Selecione uma opção")

        # Rótulo
        label = tk.Label(self.root, text="Escolha a função a executar:")
        label.pack(pady=10)

        # Caixa de seleção
        menu = tk.OptionMenu(self.root, self.opcao_var, *self.opcoes)
        menu.pack(pady=10)

        # Botão para confirmar
        botao = tk.Button(self.root, text="Executar", command=self.get_opcao_selecionada)
        botao.pack(pady=20)

        # Inicia a interface gráfica
        self.root.mainloop()

    def get_opcao_selecionada(self):
        self.resultado = self.opcao_var.get()
        print(f"Função selecionada: {self.resultado}")
        self.root.destroy()  # Fecha a janela

