

#definindo a classe principal e seus atributos
class Livro():
    def __init__(self, titulo, autor, gênero, estoque): 
        self.titulo = titulo
        self.autor = autor
        self.gênero = gênero
        self.estoque = estoque
        self.acervo = {} #definindo a lista vazia que receberá os livros que já existem
        self.novoAcervo = [] #definindo a lista que recebe os novos livros
    
    #Função para cadastrar novos livros
    def Cadastro(self, livro, autor, gênero, estoque):
        livro_novo = Livro(livro, autor, gênero, estoque)
        self.novoAcervo.append(livro_novo)

    #Função para listar todos os livros
    def __str__(self):
        return f"Os livros são {self.titulo}"
        
    #Função para realizar a busca dos livros
    def Busca(self, livro):
        pass

    #Função para gerar o gráfico com as informações 
    def Gerar_Gráfico(self, dados):
        pass    


livro1 = Livro("O Chamado de Cthulhu", "Lovecraft", "Terror Cósmico", 1)
livro2 = Livro("Sussurros na Escuridão", "Lovecraft", "Terror Cósmico", 5)
livro3 = Livro("Tudo que Destruimos", "Mayra", "Drama", 12)
adicionar_Livro = livro1.Cadastro("O Pequeno Principe", "Antoine de Saint-Exupéry", "Fábula", 100)
adicionar_Livro2 = livro1.Cadastro("A Culpa é das Estrelas", "John Green", "Romance", 50)
print(livro1)