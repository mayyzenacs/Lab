#Faça um programa que peça ao usuário para digitar 10 valores e mostre a soma deles.

numeros = [] 

while len(numeros) < 10: 
    numeros.append(int(input("Digite um numero: ")))

soma = 0

for n in numeros:
    soma += n

print(f"Os seus numeros escolhidos foram {numeros}")
print(f"A soma deles resulta em: {soma}")