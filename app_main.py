import matplotlib.pyplot as plt

#definindo a classe principal e seus atributos
class Livro():
    def __init__(self, titulo, autor, gênero, estoque): 
        self.titulo = titulo
        self.autor = autor
        self.gênero = gênero
        self.estoque = estoque

    #Função para listar todos os livros que é chamada quando a opção de listar acervo é escolhida
    def __str__(self):
        return f"Livro: {self.titulo} Autor: {self.autor} Gênero: {self.gênero} Estoque: {self.estoque}"
    
    #Função para gerar o gráfico com as informações 
    def Gerar_Gráfico(self, dados):
        pass   

acervo = []          #definindo a lista que recebe os novos livros

#Função para realizar a busca dos livros
def Busca(titulo):
    for livro in acervo: #percorre a lista, lembrando que a lista tem cada instacia atribuida a classe 
        if livro.titulo.lower() == titulo.lower(): #vai verificar utilizando a instancia dentro da lista
            print()
            print(f"--> livro {livro.titulo} ENCONTRADO! \n --> ESTOQUE: {livro.estoque}")
            return livro
        else:
            print()
            print("livro não encontrado")

#Função para cadastrar novos livros
def Cadastro(titulo, autor, gênero, estoque):
    adicionar_livro = Livro(titulo, autor, gênero, estoque)
    acervo.append(adicionar_livro)
    print(f"Livro {titulo} do autor {autor} adicionado com sucesso")

#Função para mostrar a lista completa de livros adicionados
def listarAcervo():
    for livro in acervo:
        print("==========")
        print(livro)

print("=======================================================")
print("===================BIBLIOTECA ONLINE===================")
print("=======================================================")

#loop que torna possivel o menu de opções e a possibilidade de selecionar outras opções
while True:
    print()
    print("____________ MENU ____________")
    print("""
          1 - Adicionar livro\n 
          2 - Listar acervo \n 
          3 - Buscar Livro \n 
          4 - Gerar Gráfico \n 
          0 - SAIR
          """)
    entrada = int(input("Digite uma opção númerica: "))
    
    #esse if verifica qual opção foi digitada e resolve o resultado
    if entrada == 1:
        titulo = input("Digite TITULO: ").upper()
        autor = input("Digite AUTOR: ").upper()
        genero = input("Digite GÊNERO: ").upper()
        estoque = int(input("Digite ESTOQUE: "))
        Cadastro(titulo, autor, genero, estoque)
        
    elif entrada == 2:
        print("ESTOQUE TOTAL")
        print()
        listarAcervo() #chama a função listar acervo la de cima para mostrar a lista
    elif entrada == 3:
        Busca(input("Digite o titulo do livro: ")) #recebe o nome do livro a buscar e manda para função de busca     
    elif entrada == 4:
      generos = []
      for instancia in acervo:
          generos(instancia.gênero)
          cont = generos.count(instancia.gênero)
      plt.bar(generos, cont, color="blue")
      plt.xlabel("Gêneros")
      plt.ylabel("Quantidade")
      plt.title("Livros por gênero")
    elif entrada == 0:
        print()
        print("Programa Encerrado!")
        print("====================")
        break


