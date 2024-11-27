from abc import ABC, abstractmethod

# Padrão Template Method: Define uma estrutura base para os produtos, que será especializada por subclasses.
class Produto(ABC):
    @abstractmethod
    def __init__(self, nome):
        self.nome = nome

class ProdutoPerecivel(Produto):
    def __init__(self, nome, data_validade):
        super().__init__(nome)
        self.data_validade = data_validade
        self.tipo = "Perecível"

class ProdutoNaoPerecivel(Produto):
    def __init__(self, nome):
        super().__init__(nome)
        self.tipo = "Não Perecível"

class ProdutoDigital(Produto):
    def __init__(self, nome, tamanho_arquivo):
        super().__init__(nome)
        self.tamanho_arquivo = tamanho_arquivo
        self.tipo = "Digital"

# Padrão Factory Method: Encapsula a criação de diferentes tipos de produtos.
class FabricaDeProdutos:
    @staticmethod
    def criar_produto(tipo_produto, nome, **kwargs):
        if tipo_produto == "perecivel":
            return ProdutoPerecivel(nome, kwargs.get("data_validade"))
        elif tipo_produto == "nao_perecivel":
            return ProdutoNaoPerecivel(nome)
        elif tipo_produto == "digital":
            return ProdutoDigital(nome, kwargs.get("tamanho_arquivo"))
        else:
            raise ValueError("Tipo de produto desconhecido!")
