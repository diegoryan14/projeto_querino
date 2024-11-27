from inventory import Estoque
from product import FabricaDeProdutos
from transaction import Transacao

def adicionar_produtos(estoque):
    while True:
        print("\n--- Adicionar Produto ao Estoque ---")
        tipo_produto = input(
            "Digite o tipo de produto (perecivel, nao_perecivel, digital): "
        ).strip().lower()
        
        nome = input("Digite o nome do produto: ").strip()
        
        if tipo_produto == "perecivel":
            data_validade = input("Digite a data de validade (YYYY-MM-DD): ").strip()
            produto = FabricaDeProdutos.criar_produto(tipo_produto, nome, data_validade=data_validade)
        elif tipo_produto == "digital":
            tamanho_arquivo = input("Digite o tamanho do arquivo (ex: 2GB): ").strip()
            produto = FabricaDeProdutos.criar_produto(tipo_produto, nome, tamanho_arquivo=tamanho_arquivo)
        elif tipo_produto == "nao_perecivel":
            produto = FabricaDeProdutos.criar_produto(tipo_produto, nome)
        else:
            print("Tipo de produto inválido. Tente novamente.")
            continue

        quantidade = int(input(f"Digite a quantidade de {nome}: "))
        estoque.adicionar_produto(produto, quantidade)

        continuar = input("Deseja adicionar outro produto? (s/n): ").strip().lower()
        if continuar != "s":
            break

def registrar_vendas(transacao):
    while True:
        print("\n--- Registrar Venda ---")
        nome_produto = input("Digite o nome do produto: ").strip()
        quantidade = int(input("Digite a quantidade vendida: "))
        preco = float(input("Digite o preço unitário do produto (R$): "))
        
        transacao.registrar_venda(nome_produto, quantidade, preco)

        continuar = input("Deseja registrar outra venda? (s/n): ").strip().lower()
        if continuar != "s":
            break

if __name__ == "__main__":
    estoque = Estoque()

    adicionar_produtos(estoque)

    print("\nProdutos adicionados ao estoque:")
    estoque.listar_produtos()

    transacao = Transacao()
    registrar_vendas(transacao)

    print("\nEstoque atualizado após vendas:")
    estoque.listar_produtos()
