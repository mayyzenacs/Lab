#Faça uma função que receba um valor inteiro n ≥ 0 e calcule o seu fatorial n!. Lembrete: 0! = 1.

def fatorial(n):
    
    for n in range(0, num +1):
        resultado = n*n

    return resultado




while True:
    num = int(input("numero inteiro "))
    if num >= 0:
        break
    else:
        print("Precisa ser de 0 a N")


print(fatorial(num))