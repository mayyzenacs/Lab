#Faça um algoritmo que leia um número N, some todos os números inteiros de 1 a N, e mostre o resultado obtido.

contador = []

num = int(input("digite um numero "))

cont = 0

while cont != num:
    cont += 1
    contador.append(cont)

print(contador)
print(f"{sum(contador)}")