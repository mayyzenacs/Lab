from django.db import models

# Create your models here.
class Evento():
    def __init__(self, nome, categoria, local=None, link= None):
        self.nome = nome
        self.categoria = categoria
        self.local = local
        self.link = link

aula_python = Evento('aula python', 'backend', 'local 1')
aula_java = Evento('aula java', 'orientada objetos', 'online')
eventos = [
    aula_python,
    aula_java
]