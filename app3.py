
import random
sorteios = ['sorteio 1', 'sorteio 2', 'sorteio 3']
participantes = ['lucas', 'ana', 'felipe', 'carol', 'mayra','kevin','carlos']

ganhador = {sorteio: random.choice(participantes)
for sorteio in sorteios}

print(ganhador)
