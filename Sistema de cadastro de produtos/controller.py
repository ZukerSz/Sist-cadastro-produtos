from model import ProdutoBase, ProdutoEletronico, ProdutoAlimento, ProdutoModel
from view import ProdutoView

class ProdutoController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.cadastrar_button.config(command=self.adicionar_produto)  # Configura o botão para chamar adicionar_produto ao ser clicado
        self.atualizar_lista()  # Atualiza a lista de produtos na interface

    def adicionar_produto(self):
        # Obtém os dados do formulário de cadastro
        tipo = self.view.tipo_combobox.get()
        nome = self.view.nome_entry.get()
        marca = self.view.marca_entry.get()
        preco = self.view.preco_entry.get()
        extra = self.view.extra_entry.get()

        # Verifica se todos os campos obrigatórios foram preenchidos
        if tipo and nome and marca and preco:
            # Cria o produto apropriado com base no tipo selecionado
            if tipo == "Eletrônico" and extra:
                produto = ProdutoEletronico(nome, marca, preco, extra)
            elif tipo == "Alimento" and extra:
                produto = ProdutoAlimento(nome, marca, preco, extra)
            else:
                produto = ProdutoBase(nome, marca, preco)

            self.model.adicionar_produto(produto)  # Adiciona o produto ao modelo
            self.atualizar_lista()  # Atualiza a lista de produtos na interface

    def atualizar_lista(self):
        # Limpa a lista atual de produtos na interface
        for row in self.view.tree.get_children():
            self.view.tree.delete(row)
        
        # Preenche a lista com os produtos do modelo
        for produto in self.model.listar_produtos():
            if isinstance(produto, ProdutoEletronico):
                tipo = "Eletrônico"
                garantia_validade = f"Garantia: {produto.garantia}"
                detalhes = f"Detalhes: {produto.get_detalhes()}"
            elif isinstance(produto, ProdutoAlimento):
                tipo = "Alimento"
                garantia_validade = f"Validade: {produto.validade}"
                detalhes = f"Detalhes: {produto.get_detalhes()}"
            else:
                tipo = ""
                garantia_validade = ""
                detalhes = ""

            # Insere o produto na tabela da interface
            self.view.tree.insert("", "end", values=(produto.nome, produto.marca, produto.preco, tipo, garantia_validade, detalhes))
