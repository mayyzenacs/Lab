# list [2, 4, 6, 8, 10]

lista = [i for i in range(1,11) if i % 2]                                
print(lista)


lista_base = ['vermelho', 'azul', 'verde', 'amarelo', 'rosa', 'preto']
print([str(lista_base.index(i)+1)+ '-' + i for i in lista_base])
#a