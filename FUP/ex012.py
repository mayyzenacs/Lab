#Escreva uma função que receba n e k tais que k ≥ 0 e n ≥ k e calcule o coeficiente binomial Cn,k = n!/(k!*(n-k)!)

def binominal(n, k):
    n1 = k1 = na1 = 1
    for n in range(0, n+ 1):
        n1 = n*n
    for k in range(0, k+1):
        k1 = k*k
    no = n - k
    for na in range(0, no +1):
        na1 = no * no
    
    return n1 / (k1 * na1)

while True:
    num1 = int(input("Numero 1"))
    num2 = int(input("numero 2"))

    if num1 >= 0 and num2 > num1:
        print(binominal(num1, num2))
        break
    else:
        print("tente novamente")
    