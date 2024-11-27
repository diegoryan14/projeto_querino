import functools
from inventory import Estoque

# Padrão Decorator: Adiciona funcionalidades de desconto a um método sem modificar sua implementação original.
def desconto_transacao(porcentagem_desconto):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(self, nome_produto, quantidade, preco, **kwargs):
            preco_com_desconto = preco - (preco * porcentagem_desconto / 100)
            print(f"Desconto aplicado: {porcentagem_desconto}% - Preço final: R${preco_com_desconto:.2f}")
            return func(self, nome_produto, quantidade, preco_com_desconto, **kwargs)
        return wrapper
    return decorator

# Padrão Decorator: Adiciona funcionalidades de imposto a um método sem modificar sua implementação original.
def imposto_transacao(taxa_imposto):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(self, nome_produto, quantidade, preco, **kwargs):
            preco_com_imposto = preco + (preco * taxa_imposto / 100)
            print(f"Imposto aplicado: {taxa_imposto}% - Preço final: R${preco_com_imposto:.2f}")
            return func(self, nome_produto, quantidade, preco_com_imposto, **kwargs)
        return wrapper
    return decorator

class Transacao:
    def __init__(self):
        self.estoque = Estoque()  # Padrão Singleton: Obtém a instância única de Estoque.

    @imposto_transacao(5)
    @desconto_transacao(10)
    def registrar_venda(self, nome_produto, quantidade, preco):
        """Registra uma venda de um produto."""
        if self.estoque.remover_produto(nome_produto, quantidade):
            preco_total = preco * quantidade
            print(f"Venda registrada: {nome_produto}, {quantidade} unidades, Total: R${preco_total:.2f}")
        else:
            print("Erro ao registrar a venda.")
