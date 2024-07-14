#Faça um programa que leia 10 inteiros e imprima sua média.

notas = []
soma_notas = 0

while len(notas) < 10:
    notas.append(float(input("Digite uma nota ")))

for nota in notas: 
    soma_notas += nota

resultado = soma_notas + len(notas)
print(resultado)