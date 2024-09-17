#este programa tem como objetivo calcular a média de notas que forem inseridas pelo úsuario

# Implentação da função que fará o cálculo
def calcula_media(notas): #a função recebe a lista notas a partir do parâmetro notas
    soma = 0 #defini a  variável soma como - que vai receber cada nota no loop for
    for nota in notas: #loop que percorre toda a lista notas
        soma += nota #soma cada nota inserindo essa soma dentro da variável soma
    media = soma / len(notas) #utiliza o valor da variável soma para dividir pelo tamanho da lista notas, assim obtendo a média
    if media >= 7: #checa se média é maior ou igual a 7
        return f"{media:.2f} SITUAÇÃO: Aluno APROVADO" #retorna a media e a situação
    else: #caso não seja maior ou igual a 7 cai nessa condição
        return f"{media:.2f} SITUAÇÃO: Aluno REPROVADO"


notas = [] #defini a lista notas 

print("Bem vindo ao programa de calculo de média") #print introdutorio 

while True:  #while true para checar informações e receber várias notas
    confirm = int(input("Digite 1 para continuar e 0 para sair: ")) #habilita a possibilidade de receber N notas

    if confirm == 1: #checa se o úsuario gostaria de continuar ou não
        notas.append(float(input("Digite uma nota: "))) #recebe a nota e a adiciona dentro da lista, recebe um tipo de dado float
    elif confirm == 0:
        print("Programa encerrado")
        print(40*"~=")
        #neste bloco encerra o programa e resolve o restante, apresenta as notas que foram inseridas
        #E chama a função mandando para ela as notas que estão dentro da lista
        print(f"As notas inseridas foram {notas} e a média foi: {calcula_media(notas)}")
        print(40*"~=") 
        break #interrompe o loop ao ser digitado 0
