import os

# print(os.name) #listar OS
# print(os.listdir) #listar arquivos no diretorio atual
# print(os.getcwd) #retorna o path do diretorio atual
# print(os.sep) #retorna o separador do sistema
# print(os.path.join(os.getcwd() + os.sep + "nomearquivo.txt")) #reotnra path do arquivo
# print(os.path.join(os.getcwd() + os.sep + "pasta" + "nomearquivo")) #reotnra um arquivo dentro de uma pasta 

desafio_arquivos = os.path.join(os.getcwd()+ os.sep + "Pythonista" + os.sep + "desafio_arquivos")

boleto = os.path.join(os.getcwd()+ os.sep + "Pythonista" + os.sep + "desafio_arquivos" + os.sep + "boleto.pdf")
roteiro = os.path.join(os.getcwd()+ os.sep + "Pythonista" + os.sep + "desafio_arquivos" + os.sep + "roteiro.txt")
planilha = os.path.join(os.getcwd()+ os.sep + "Pythonista" + os.sep + "desafio_arquivos" + os.sep + "planilha.xlsx")

texto = os.path.join(os.getcwd()+ os.sep + "Pythonista" + os.sep + "desafio_arquivos" + os.sep + "desafio_arquivos_texto" + os.sep + "texto_1.txt")

diretorio = "desafio_arquvios"
print(os.listdir(desafio_arquivos))
print(boleto)
print(planilha)
print(roteiro)

print("="*20)

print(texto)

os.mkdir("musicas")
os.makedirs("musicas"+ os.sep + "rock") 