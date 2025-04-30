class Produtos:
    def __init__(self, nome, preço, estoque, descrição):
        self.nome = nome
        self.preço = preço
        self.estoque = estoque
        self.descrição = descrição


    def descontar_estoque(self, estoque):
        if estoque >= self.estoque:
            self.estoque -= estoque
        else:
            return print("não temos estoque suficiente")

    def aumentar_estoque(self, estoque):
        self.estoque += estoque
    
    def __str__(self):
        return f"Lista de Produtos: {self.nome}, {self.preço}$, estoque:{self.estoque}, descrição: {self.descrição}"

class Clientes:
    def __init__(self, nome, endereço):
        self.nome = nome
        self.endereço = endereço
        self.historico_compras = []

    def realizar_pedido(self, pedido):
        self.historico_compras.append(pedido)

    def contar_pedidos(self):
        return len(self.historico_compras)

    def __str__(self):
        compras_str = ",".join([str(pedido) for pedido in self.historico_compras])  
        return f"Cliente: {self.nome}, endereço: {self.endereço}, compras: {compras_str}"

class Pedidos:
    def __init__(self, cliente,lista_produtos, data):
        self.cliente = cliente
        self.lista_produtos = lista_produtos
        self.data = data
        cliente.realizar_pedido(self)

    def calcular_total(self):
        return sum(produto.preço for produto in self.lista_produtos)
    

produto1 = Produtos("parafusadeira", 250, 10, "parafusadeira 12v")
produto2 = Produtos("Lixadeira Orbital", 350, 20, "Lixadeira Orbital 220v")
produto3 = Produtos("Jogo Soquetes", 99.9, 200, "Jogo de soquetes 32 pçs")


cliente1 = Clientes("Carlos", "Rua Benedito, 12")
cliente2 = Clientes("Renata", "Rua Suslis, 234")
cliente3 = Clientes("Leandro", "Av Joao Renan, 1234, Bloco B")

pedido1 = Pedidos(cliente1,[produto1, produto3], "23-05-2024")
pedido2 = Pedidos(cliente1, [produto2],"03-01-2023")
pedido2 = Pedidos(cliente2,[produto1, produto2], "12-09-2024")
pedido3 = Pedidos(cliente3, [produto3],"29-03-1999")

print(f"Cliente: {cliente1.nome} numero de pedidos: {cliente1.contar_pedidos()}")
print(f"Cliente: {cliente2.nome} numero de pedidos: {cliente2.contar_pedidos()}")
print(f"Cliente: {cliente3.nome} numero de pedidos: {cliente3.contar_pedidos()}")


print(pedido1.calcular_total())
print(pedido2.calcular_total())
print(pedido3.calcular_total())



print("teste")

