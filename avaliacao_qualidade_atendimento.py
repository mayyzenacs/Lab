import numpy as np
import matplotlib.pyplot as plt

plt.style.use('default')
plt.rcParams['figure.figsize'] = (10,6)

def tempo_rapido(x):
  # função de pertinência para tempo rápido (0-15 min)
  if x <= 10:
    return 1.0
  elif x <= 20:
    return (20 - x) / 10
  else:
    return 0.0
def tempo_medio(x):
  # função de pertinencia para tempo médio (10-30 min)
  if x <= 10:
    return 0.0
  elif x <= 20:
    return (x-10) / 10
  elif x <= 30:
    return (30 - x) / 10
  else:
    return 0.0
def tempo_lento(x):
  # função de tempo lento (25-60 min)
  if x <= 25:
    return 0.0
  elif x <= 35:
    return (x - 25) / 10
  else:
    return 1.0

def cordialidade_baixa(x):
  if x <= 3:
    return 1.0
  elif x <= 5:
    return (5 - x) / 2
  else:
    return 0.0
def cordialidade_media(x):
  if x <= 3:
    return 0.0
  elif x <= 5:
    return (x - 3) / 2
  elif x <= 7:
    return (7 - x) / 2
  else:
    return 0.0
def cordialidade_alta(x):
  if x <= 6:
    return 0.0
  elif x <= 8:
    return (x - 6) / 2
  else:
    return 1.0

def avaliar_atendimento(tempo, cordialidade):
  t_rapido = tempo_rapido(tempo)
  t_medio = tempo_medio(tempo)
  t_lento = tempo_lento(tempo)

  c_baixa = cordialidade_baixa(cordialidade)
  c_media = cordialidade_media(cordialidade)
  c_alta = cordialidade_alta(cordialidade)

  excelente = min(t_rapido, c_baixa)
  boa = max(min(t_rapido, c_media), min(t_medio, c_alta))
  regular = min(t_medio, c_media)
  ruim = max(min(t_lento, c_baixa), min(t_lento, c_media), min(t_lento, c_alta), min(t_rapido, c_baixa), min(t_medio, c_baixa))

  qualidade_final = (excelente * 9 + boa * 7 + regular * 5 + ruim * 2) / max(excelente + boa + regular + ruim, 0.001)
  return {
      'excelente': excelente,
      'boa': boa,
      'regular': regular,
      'ruim': ruim,
      'qualidade_final': qualidade_final
  }

def testar_sistema():
  casos_teste = [
      {"tempo": 8, "cordialidade": 9, "descrição": "Atendimento rápido e muito cordial"}, {"tempo": 15, "cordialidade": 6, "descrição": "Atendimento médio"}, {"tempo": 35, "cordialidade": 3, "descrição": "Atendimento demorado e pouco cordial"}, {"tempo": 12, "cordialidade": 8, "descrição": "Bom atendimento geral"} 
    ]

  print("===TESTE DO SISTEMA DE LÓGICA NEBULOSA===\n")

  for i, caso in enumerate(casos_teste, 1):
    resultado = avaliar_atendimento(caso['tempo'], caso['cordialidade'])
    print(f"Caso {i} : {caso['descrição']}")
    print(f"Tempo de espera: {caso['tempo']} minutos")
    print(f"Cordialidade: {caso['cordialidade']}/10")
    print("Graus de pertinência:")
    print(f"Excelente: {resultado['excelente']}")
    print(f"Boa: {resultado['boa']}")
    print(f"Regular: {resultado['regular']}")
    print(f"Ruim: {resultado['ruim']}")
    print(f"Qualidade final: {resultado['qualidade_final']}/10\n")

testar_sistema()

def plotar_funcoes_pertinencia():
  tempo_range = np.linspace(0, 60, 100)
  plt.figure(figsize=(15, 5))

  plt.subplot(1, 3, 1)
  plt.plot(tempo_range, [tempo_rapido(t) for t in tempo_range], 'g-', label='Rápido', linewidth=2)
  plt.plot(tempo_range, [tempo_medio(t) for t in tempo_range], 'y-', label='Médio', linewidth=2)
  plt.plot(tempo_range, [tempo_lento(t) for t in tempo_range], 'r-', label='Lento', linewidth=2)
  plt.title('Tempo de Espera')
  plt.xlabel('Minutos')
  plt.ylabel('Grau de Pertinência')
  plt.legend()
  plt.grid(True, alpha=0.3)

  # Cordialidade
  cord_range = np.linspace(0, 10, 100)
  plt.subplot(1, 3, 2)
  plt.plot(cord_range, [cordialidade_baixa(c) for c in cord_range], 'r-.', label='Baixa', linewidth=2)
  plt.plot(cord_range, [cordialidade_media(c) for c in cord_range], 'y-', label='Média', linewidth=2)
  plt.plot(cord_range, [cordialidade_alta(c) for c in cord_range], 'g-', label='Alta', linewidth=2)
  plt.title('Cordialidade')
  plt.xlabel('Nível')
  plt.ylabel('Grau de Pertinência')
  plt.legend()
  plt.grid(True, alpha=0.3)
  # Superfície de qualidade
  plt.subplot(1, 3, 3)
  T, C = np.meshgrid(np.linspace(0, 60, 30), np.linspace(0, 10, 30))
  Z = np.zeros_like(T)

  for i in range(T.shape[0]):
    for j in range(T.shape[1]):
        resultado = avaliar_atendimento(T[i, j], C[i, j])
        Z[i, j] = resultado['qualidade_final']

  contour = plt.contourf(T, C, Z, levels=20, cmap='RdYlGn')
  plt.colorbar(contour)
  plt.title('Superfície de Qualidade')
  plt.xlabel('Tempo (min)')
  plt.ylabel('Cordialidade')

  plt.tight_layout()
  plt.show()

plotar_funcoes_pertinencia()