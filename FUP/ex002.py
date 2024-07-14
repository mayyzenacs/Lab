#Escreva um programa que imprima os números de 0 até 100000 (cem mil), de 1000 em 1000.

from time import sleep

num = 0

while num < 100000: 
    num += 1000
    sleep(0.5)
    print(num)