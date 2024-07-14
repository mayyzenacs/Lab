#10. Faça uma função que receba um inteiro x e um inteiro não-negativo n e, usando laço de repetição, calcule xn e retorne o resultado.

def inteiro(x, y):
    return x ** y


num1 = int(input("Digite um numero inteiro "))

while True:
    num2 = int(input("digite outro numero nao negativo"))
    if num2 <= -1:
        print("digite um numero Não Negativo")
    else:
        break

final = inteiro(num1,num2)
print(final)