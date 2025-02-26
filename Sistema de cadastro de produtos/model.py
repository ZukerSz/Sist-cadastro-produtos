import pickle

class ProdutoBase:
    def __init__(self, nome, marca, preco):
        self._nome = nome
        self._marca = marca
        self._preco = preco

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, valor):
        self._marca = valor

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor):
        self._preco = valor

    # Polimorfismo: Método que pode ser sobrescrito por subclasses para fornecer mais detalhes
    def get_detalhes(self):
        return f"{self.nome}, {self.marca}, {self.preco}"

# Herança: ProdutoEletronico herda de ProdutoBase
class ProdutoEletronico(ProdutoBase):
    def __init__(self, nome, marca, preco, garantia):
        super().__init__(nome, marca, preco)  # Chama o construtor da classe base
        self._garantia = garantia

    @property
    def garantia(self):
        return self._garantia

    @garantia.setter
    def garantia(self, valor):
        self._garantia = valor

    # Polimorfismo: Sobrescreve get_detalhes para adicionar informações específicas
    def get_detalhes(self):
        return f"{super().get_detalhes()}, Garantia: {self.garantia}"

# Herança: ProdutoAlimento herda de ProdutoBase
class ProdutoAlimento(ProdutoBase):
    def __init__(self, nome, marca, preco, validade):
        super().__init__(nome, marca, preco)  # Chama o construtor da classe base
        self._validade = validade

    @property
    def validade(self):
        return self._validade

    @validade.setter
    def validade(self, valor):
        self._validade = valor

    # Sobrecarga simulada: Método especial para manipulação de atributos ao desserializar objetos
    def __setstate__(self, state):
        self.__dict__.update(state)
        if '_validade' not in self.__dict__:
            self._validade = None

    # Polimorfismo: Sobrescreve get_detalhes para adicionar informações específicas
    def get_detalhes(self):
        return f"{super().get_detalhes()}, Validade: {self.validade}"

class ProdutoModel:
    def __init__(self):
        self.produtos = []
        self.carregar_dados()  # Carrega dados salvos ao iniciar

    def adicionar_produto(self, produto):
        self.produtos.append(produto)
        self.salvar_dados()  # Salva os dados ao adicionar um novo produto

    def listar_produtos(self):
        return self.produtos  # Retorna a lista de produtos

    def salvar_dados(self):
        # Salva os produtos em um arquivo usando pickle
        with open('produtos.pkl', 'wb') as file:
            pickle.dump(self.produtos, file)

    def carregar_dados(self):
        try:
            # Carrega os produtos de um arquivo usando pickle
            with open('produtos.pkl', 'rb') as file:
                self.produtos = pickle.load(file)
        except FileNotFoundError:
            self.produtos = []
