#Faça um programa que leia um número inteiro N e depois imprima os N primeiros números naturais ímpares.

num = int(input("digite um numero inteiro "))

cont = 0
numeros = 0 

while cont < num: 
    numeros += 2
    cont += 1
    print(numeros)
