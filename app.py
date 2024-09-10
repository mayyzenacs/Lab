class Produtos:
    def __init__(self, produtos, preço, estoque, descrição):
        self.produtos = produtos
        self.preço = preço
        self.estoque = estoque
        self.descrição = descrição

    def descontar_estoque(self, estoque):
        pass

    def aumentar_estoque(self, estoque):
        pass

class Clientes:
    def __init__(self, nome, endereço, historico_compras):
        self.nome = nome
        self.endereço = endereço
        self.historico_compras = historico_compras

        def realizar_compra(self, historico_compras):
            pass

class Pedidos:
    def __init__(self, cliente,lista_produtos, data):
        self.cliente = cliente
        self.lista_produtos = lista_produtos
        self.data = data

    def calcular_total(self, cliente, lista_produtos):
        pass


Produtos("parafusadeira", 250, 10, "parafusadeira 12v")


