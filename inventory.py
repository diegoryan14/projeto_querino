class Estoque:
    # Padrão Singleton: Garante que apenas uma instância de Estoque será criada.
    _instancia = None

    def __new__(cls, *args, **kwargs):
        # Controle da criação de instância única
        if not cls._instancia:
            cls._instancia = super(Estoque, cls).__new__(cls, *args, **kwargs)
            cls._instancia.produtos = {}
        return cls._instancia

    def adicionar_produto(self, produto, quantidade):
        """Adiciona um produto ao estoque ou atualiza sua quantidade."""
        if produto.nome in self.produtos:
            self.produtos[produto.nome]["quantidade"] += quantidade
        else:
            self.produtos[produto.nome] = {"produto": produto, "quantidade": quantidade}

    def remover_produto(self, nome_produto, quantidade):
        """Remove uma quantidade específica de um produto do estoque."""
        if nome_produto in self.produtos:
            if self.produtos[nome_produto]["quantidade"] >= quantidade:
                self.produtos[nome_produto]["quantidade"] -= quantidade
                if self.produtos[nome_produto]["quantidade"] == 0:
                    del self.produtos[nome_produto]
                return True
            else:
                print(f"Erro: Estoque insuficiente para {nome_produto}.")
        else:
            print(f"Erro: Produto {nome_produto} não encontrado no estoque.")
        return False

    def verificar_estoque(self, nome_produto):
        """Retorna a quantidade em estoque de um produto."""
        if nome_produto in self.produtos:
            return self.produtos[nome_produto]["quantidade"]
        return 0

    def listar_produtos(self):
        """Exibe todos os produtos disponíveis no estoque."""
        if not self.produtos:
            print("\n--- Estoque vazio ---")
        else:
            print("\n--- Estoque Atual ---")
            for nome, detalhes in self.produtos.items():
                print(
                    f"{nome}: {detalhes['quantidade']} unidades ({detalhes['produto'].tipo})"
                )
