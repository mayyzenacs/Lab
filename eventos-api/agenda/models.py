from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=256, unique=True)

class Evento():
    def __init__(self, nome, categoria, local=None, link= None):
        self.nome = nome
        self.categoria = categoria
        self.local = local
        self.link = link

aula_python = Evento('aula python', 'backend', 'local 1')
aula_java = Evento('aula java', 'orientada objetos', link="www.aula")
eventos = [
    aula_python,
    aula_java
]