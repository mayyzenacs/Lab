#Faça uma função que calcule e retorne a soma dos N primeiros números pares (considere o 0 como o primeiro número par).

num = int(input("digite um numero inteiro "))

cont = 0
par = []

while cont < num: 
    cont += 1
    if cont % 2 == 0:
        par.append(cont)

print(sum(par))
    