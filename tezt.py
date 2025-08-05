

def calculo(a, b, operador): 
    if operador == '+':
        soma = a + b
        return soma
    elif operador == '-': 
        sub = a - b 
        return sub
    elif operador == '/':
        divi = a / b
        return divi
    elif operador == '*':
        mult = a * b
        return mult
    
resultado = calculo(5, 6, '*')
print(resultado)

def test():
    assert calculo(2,6, '*') == 12

print(test)

