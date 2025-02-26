import tkinter as tk
from tkinter import ttk
#tkinter: É uma biblioteca padrão do Python para criação de interfaces gráficas.
#ttk: Módulo dentro do tkinter que fornece widgets com um estilo melhorado.

#O código define uma interface gráfica usando Tkinter para cadastro de produtos.
#Inclui uma tabela (ttk.Treeview) para exibição dos produtos cadastrados e um formulário (Labels, Entry, Combobox, Button) para inserir novos produtos. 
# Cada componente é configurado e adicionado à janela principal (root).

class ProdutoView:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Produtos")
        #ProdutoView: É uma classe que representa a visualização para cadastro de produtos na interface gráfica.
        #__init__: Método construtor da classe que inicializa a janela principal (root) com o título "Cadastro de Produtos".

        # Tabela de produtos
        self.tree = ttk.Treeview(root, columns=("Nome", "Marca", "Preço", "Tipo", "Garantia/Validade", "Detalhes"), show="headings")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Marca", text="Marca")
        self.tree.heading("Preço", text="Preço")
        self.tree.heading("Tipo", text="Tipo")
        self.tree.heading("Garantia/Validade", text="Garantia/Validade")
        self.tree.heading("Detalhes", text="Detalhes")
        #ttk.Treeview: É um widget que exibe dados hierárquicos, como uma tabela.
        #columns: Define as colunas da tabela.
        #show="headings": Especifica que apenas os cabeçalhos das colunas serão exibidos.
        #self.tree.heading(): Define os títulos das colunas na tabela.

        # Ajusta a largura das colunas da tabela
        self.tree.column("Nome", width=150)
        self.tree.column("Marca", width=150)
        self.tree.column("Preço", width=100)
        self.tree.column("Tipo", width=100)
        self.tree.column("Garantia/Validade", width=150)
        self.tree.column("Detalhes", width=400)
        #self.tree.column(): Define a largura das colunas da tabela para melhor exibição dos dados.

        self.tree.pack()  # Adiciona a tabela na janela
        #self.tree.pack(): Empacota (adiciona) a tabela na janela principal (root) que está no arquivo "main"

        # Formulário de cadastro de produtos
        self.tipo_label = tk.Label(root, text="Tipo:")
        self.tipo_label.pack()
        self.tipo_combobox = ttk.Combobox(root, values=["Eletrônico", "Alimento"])
        self.tipo_combobox.pack()

        self.nome_label = tk.Label(root, text="Nome:")
        self.nome_label.pack()
        self.nome_entry = tk.Entry(root)
        self.nome_entry.pack()

        self.marca_label = tk.Label(root, text="Marca:")
        self.marca_label.pack()
        self.marca_entry = tk.Entry(root)
        self.marca_entry.pack()

        self.preco_label = tk.Label(root, text="Preço:")
        self.preco_label.pack()
        self.preco_entry = tk.Entry(root)
        self.preco_entry.pack()

        self.extra_label = tk.Label(root, text="Garantia/Validade:")
        self.extra_label.pack()
        self.extra_entry = tk.Entry(root)
        self.extra_entry.pack()

        self.cadastrar_button = tk.Button(root, text="Cadastrar")
        self.cadastrar_button.pack()
        #Criação de diversos elementos de interface para o formulário de cadastro de produtos:
        #tk.Label: Rótulo para identificar o campo.
        #ttk.Combobox e tk.Entry: Caixa de combinação e entrada para inserção de dados.
        #tk.Button: Botão para acionar a função de cadastro.
