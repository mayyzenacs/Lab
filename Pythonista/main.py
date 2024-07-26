vagas = [
    ["vaga 1", 2900],
    ["vaga 2", 1200],
    ["vaga 3", 5000]
]

def compara_salario(vagas):
    if vagas[1] >= 2500:
        return True
    else:
        return False
    
print(list(filter(compara_salario, vagas)))