import tkinter as tk
from model import ProdutoModel
from view import ProdutoView
from controller import ProdutoController

# Ponto de entrada principal da aplicação
if __name__ == "__main__":
    root = tk.Tk()  # Cria a janela principal da interface gráfica
    model = ProdutoModel()  # Cria a instância do model
    view = ProdutoView(root)  # Cria a instância da view, passando a janela principal
    controller = ProdutoController(model, view)  # Cria a instância do controlador, passando o model e a view
    root.mainloop()  # Inicia o loop principal da interface gráfica
