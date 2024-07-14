from turtle import *

t = Turtle()
t.speed(2)
while True: 
    direção = input("ir para frente ou costas? F: frente, C: costas, N: cancelar ").upper()
    if direção in "Ff":
        frente = int(input("quanto movimentar para frente: "))
        t.forward(frente)
        direção2 = input("direita ou esquerda? D ou E ")
        if direção2 in "dD":
            grausD = int(input("graus para direita "))
            t.right(grausD)
        elif direção2 in "Ee":
            grausE = int(input("graus para esquerda "))
            t.left(grausE)

    elif direção in "Cc":
        costas = int(input("Quanto movimentar para trás?: "))
        t.backward(costas)
        direção3 = input("direita ou esquerda? D ou E ")
        if direção3 in "dD":
            grausCD = int(input("graus para direita "))
            t.right(grausCD)
        elif direção3 in "Ee":
            grausCE = int(input("graus para esquerda "))
            t.left(grausCE)


    if direção == "CANCELAR":
        break

input()