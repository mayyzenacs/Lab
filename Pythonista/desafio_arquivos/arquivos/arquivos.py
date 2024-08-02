import os

frutas = ["carambola","mexerica","maça","uva","acerola"]
cores = ["roxo","amarelo","verde","rosa","azul"]
linguagens = {"python","java","C#","Rust","PHP"}


with open("frutas.txt", "a+", encoding="cp1252") as arquivo_frutas:
    #arquivo_frutas.write(f"\n{cores}")
    for item in frutas:
        arquivo_frutas.write(f"\n{item}")
    for cor in cores:
        arquivo_frutas.write(f"\n{cor}")
    arquivo_frutas.seek(0)
    ler = arquivo_frutas.read()
    print(ler)
        
    

with open("linguagens.txt", "a") as arquivo_linguagens:
    for item in linguagens:
        arquivo_linguagens.write(f"\n{item}")

# for i in range(5):
#     os.mkdir("arquivo")

