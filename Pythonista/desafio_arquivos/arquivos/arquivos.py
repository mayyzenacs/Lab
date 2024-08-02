import os


         
if os.path.isdir("frutas.txt") and os.path.isdir("frutas.txt") and os.path.isdir("frutas.txt"):
    print("diretorio ja ta criado")
else:
    os.mkdir("frutas.txt")
    os.mkdir("cores.txt")
    os.mkdir("linguagens.txt")

with open("frutas.txt"):