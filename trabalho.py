#importando os modulos necessários
import sqlite3
import pandas as pd

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

resultado = cursor.fetchall()
#for row in resultado:
 #   print(row)


entrada = ""
def inserir_dados(cursor, data_venda, produto, categoria, valor_venda):
    cursor.execute("INSERT INTO vendas1 (data_venda, produto, categoria, valor_venda) VALUES (?, ?, ?, ?)", (data_venda, produto, categoria, valor_venda))

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
    try:
        if entrada == 1:
            print("Adicione novos produtos ao banco de dados")
            data_venda = int(input("Data de venda: "))
            produto = input("Nome do produto: ")
            categoria = input("Categoria: ")
            valor_venda = float(input("Valor de carteira: "))
            inserir_dados(cursor, data_venda, produto, categoria, valor_venda)
        elif entrada == 2:
            pass
        elif entrada == 3:
            df = pd.read_sql_query(busca, conexao)
            print(df.describe())
        elif entrada == 4:
            pass
    finally:
        conexao.commit()
        print("Programa encerrado")



conexao.close()