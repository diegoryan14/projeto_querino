from abc import ABC, abstractmethod

# Padrão Template Method: Define uma estrutura base para os produtos, que será especializada por subclasses.
class Produto(ABC):
    @abstractmethod
    def __init__(self, nome):
        self.nome = nome  # Atributo comum para todos os produtos

# Subclasse para produtos perecíveis
class ProdutoPerecivel(Produto):
    def __init__(self, nome, data_validade):
        super().__init__(nome)
        self.data_validade = data_validade  # Atributo específico
        self.tipo = "Perecível"

# Subclasse para produtos não perecíveis
class ProdutoNaoPerecivel(Produto):
    def __init__(self, nome):
        super().__init__(nome)
        self.tipo = "Não Perecível"

# Subclasse para produtos digitais
class ProdutoDigital(Produto):
    def __init__(self, nome, tamanho_arquivo):
        super().__init__(nome)
        self.tamanho_arquivo = tamanho_arquivo  # Atributo específico
        self.tipo = "Digital"

# Padrão Factory Method: Encapsula a criação de diferentes tipos de produtos.
class FabricaDeProdutos:
    @staticmethod
    def criar_produto(tipo_produto, nome, **kwargs):
        # Retorna instâncias de subclasses específicas com base no tipo de produto.
        if tipo_produto == "perecivel":
            return ProdutoPerecivel(nome, kwargs.get("data_validade"))
        elif tipo_produto == "nao_perecivel":
            return ProdutoNaoPerecivel(nome)
        elif tipo_produto == "digital":
            return ProdutoDigital(nome, kwargs.get("tamanho_arquivo"))
        else:
            raise ValueError("Tipo de produto desconhecido!")
