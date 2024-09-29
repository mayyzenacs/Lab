#importando os modulos necessários
import sqlite3
import pandas as pd
from time import sleep
import matplotlib.pyplot as plt
import seaborn as sb

#criando a conexão com o banco de dados
conexao = sqlite3.connect("dados_vendas.db")

#definindo o ponteiro 
cursor = conexao.cursor()

# Passo 1.3: Criar uma tabela (se não existir)
cursor.execute('''
CREATE TABLE IF NOT EXISTS vendas1 (
id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
data_venda DATE,
produto TEXT,
categoria TEXT,
valor_venda REAL
)
''')
# Passo 1.4: Inserir alguns dados
cursor.execute('''
INSERT INTO vendas1 (data_venda, produto, categoria, valor_venda) VALUES
('2023-01-01', 'Produto A', 'Eletrônicos', 1500.00),
('2023-01-05', 'Produto B', 'Roupas', 350.00),
('2023-02-10', 'Produto C', 'Eletrônicos', 1200.00),
('2023-03-15', 'Produto D', 'Livros', 200.00),
('2023-03-20', 'Produto E', 'Eletrônicos', 800.00),
('2023-04-02', 'Produto F', 'Roupas', 400.00),
('2023-05-05', 'Produto G', 'Livros', 150.00),
('2023-06-10', 'Produto H', 'Eletrônicos', 1000.00),
('2023-07-20', 'Produto I', 'Roupas', 600.00),
('2023-08-25', 'Produto J', 'Eletrônicos', 700.00),
('2023-09-30', 'Produto K', 'Livros', 300.00),
('2023-10-05', 'Produto L', 'Roupas', 450.00),
('2023-11-15', 'Produto M', 'Eletrônicos', 900.00),
('2023-12-20', 'Produto N', 'Livros', 250.00);
''')

#extraindo os dados da tabela
busca = "SELECT * FROM vendas1"
cursor.execute(busca)

#pega os dados para visualização
resultado = cursor.fetchall()
#for row in resultado:
 #   print(row)

#le os dados usando pandas, principalmente na funcionalidade de ler sql 
df = pd.read_sql_query(busca, conexao)

#função que faz a lógica para inserir novos dados no banco de dados
def inserir_dados(cursor, data_venda, produto, categoria, valor_venda):
    cursor.execute("INSERT INTO vendas1 (data_venda, produto, categoria, valor_venda) VALUES (?, ?, ?, ?)", (data_venda, produto, categoria, valor_venda))
    conexao.commit()

#calcula a media da coluna valor de venda utilizando funcionalidade do pandas
def calcular_media():
    media = df["valor_venda"].mean()
    return f"A média dos valores de venda desses produtos é: ${media}"

#cria a primeira tabela utilizando matplotlib
def tabela():
    cont = "SELECT categoria, COUNT(*) as vendas FROM vendas1 GROUP BY categoria"
    df = pd.read_sql_query(cont,conexao)
    plt.bar(df["categoria"], df["vendas"], color="blue")
    plt.ylabel("Categoria")
    plt.xlabel("Total Vendas")
    plt.title("Vendas por Categoria")
    return plt.show()

#cria a segunda tabela utilizando seaborn
def grafico():
    dados = "SELECT categoria, valor_venda FROM vendas1"
    df = pd.read_sql_query(dados,conexao)
    plt.figure(figsize=(10,6))
    sb.scatterplot(data=df, x='categoria', y='valor_venda')
    plt.title('Distribuição dos Valores de Venda por Categoria')
    plt.xlabel('Categoria')
    plt.ylabel('Valor de Venda')
    return plt.show()

#defini entrada como nula para não ocorrer erro de que não existe
entrada = ""

#while para fazer o menu de opções
while entrada != 0:
    print("__________MENU__________")
    print("""
        (1) Adicionar Notas
        (2) Calcular Média
        (3) Determinar Situação
        (4) Relatório Final
        (0) SAIR
    """)
    entrada = int(input("Digite uma opção -> "))
    #try e finally para executar uma tarefa mesmo que a ultima nao tenha sido completada, e if e elif para verificar qual opção foi digitada
    try:
        if entrada == 1:
            print("Adicione novos produtos ao banco de dados")
            data_venda = input("Data de venda: ")
            produto = input("Nome do produto: ")
            categoria = input("Categoria: ")
            valor_venda = float(input("Valor de carteira: "))
            inserir_dados(cursor, data_venda, produto, categoria, valor_venda)
            print("Produto inserido com sucesso")
        elif entrada == 2:
            print(calcular_media())
        elif entrada == 3:
            print("Determinando situação...")
            sleep(5)
            print("Aqui está seu relátorio da situação")
            contagem = df["produto"].count()
            media_contagem = df['valor_venda'].mean()
            print(f"No banco de dados há o total de {contagem:.2f} produtos, sendo a média total do valor ${media_contagem:.2f}")     
        elif entrada == 4:
            print("Gerando os gráficos...")
            sleep(5)
            tabela()
            grafico()
    finally:
        #commit em todas as mudanças 
        conexao.commit()

#fecha a conexão
conexao.close()
print("programa encerrado")

