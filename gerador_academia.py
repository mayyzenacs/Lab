from random import sample

peito = ["supino vertical","supino reto/reclinado/inclinado","peck deck","crossover","pullover"]
costas = ["pulley da frente","pulley triangulo","pulley romano","remada baixa","remada cavalinho","remada unilateral","remada curvada","pulldown"]
ombros = ["desenvolvimento","elevação lateral","elevação frontal","remada alta","peck deck invertido"]
biceps = ["rosca direita halter","rosca direta barra","rosca concentrada","rosca martelo","rosca scott","rosca polia corda","rosca inclinado"]
triceps = ["triceps pulley","triceps pulley invertido","triceps corda","triceps testa","triceps frances","triceps banco"]
panturrilha = ["gemeos sentado","gemeos leg press"]
perna = ["cadeira extensora","mesa flexora","leg press","adutora","abduora","agachamento livre","agachamento hack","agachamento sumo","agachamento smith","avanço","sassy squat"]
abdomen = [""]
gluteos = [""]
cardio = [""]

'''
treino ABC
A = peito, ombros, triceps
B = costas, biceps, abdomen
C = perna completa
'''
def linha(tam=35):
    print("-"*tam)

ficha = []

a = int(input("Quantos exercícios por grupo muscular? "))    


def treinoA():
    treinoA = {}
    treinoA["peito"] = sample(peito,a)
    treinoA["ombro"] = sample(ombros,a)
    treinoA["triceps"] = sample(triceps,a)
    #print(treinoA)
    for chave, valor in treinoA.items():
        linha()
        print(f"- {chave} -".center(35))
        for exercicio in valor:
            print(f"{exercicio}")
    ficha.append(treinoA)

def treinoB():    
    treinoB = {}
    treinoB["costas"] = sample(costas,a)
    treinoB["biceps"] = sample(biceps,a)
    treinoB["perna"] = sample(perna,a)
    #print(treinoA)
    for chave, valor in treinoB.items():
        linha()
        print(f"- {chave} -".center(35))
        for exercicio in valor:
            print(f"{exercicio}")
    linha()

treinoA()
treinoB()