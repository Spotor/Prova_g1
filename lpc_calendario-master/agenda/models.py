from django.db import models

class Compromisso(models.Model):
    nome = models.CharField(max_length=128)
    dataEHoraDeInicio = models.DateTimeField(blank=True, null=True)
    motivo = models.TextField()

    def __str__(self):
        return self.nome

class AgendaMain(models.Model):
    codigo = models.CharField(max_length = 20)
    anotacao = models.TextField()
    telefone = models.CharField(max_length = 20)
    compromisso = models.ManyToManyField(Compromisso, blank = True)

    def __str__(self):
        return self.codigo

class Usuario(models.Model):
    codigo = models.CharField(max_length = 20)
    telefone = models.CharField(max_length = 20)
    nome = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    agenda = models.ManyToManyField(AgendaMain, blank = True)

    def __str__(self):
        return self.nome + self.codigo

class AgendaPublica(AgendaMain):
    tipo = models.CharField(max_length = 100)

    def __str__(self):
        return self.tipo

class AgendaPrivada(AgendaMain):
    tipo = models.CharField(max_length = 100)

    def __str__(self):
        return self.tipo

class Empresa(models.Model):
    nome = models.CharField(max_length = 100)
    cidade = models.CharField(max_length = 20)
    uf = models.CharField(max_length = 2)
    endereco = models.CharField(max_length = 20)
    cep = models.CharField(max_length = 12)

    def __str__(self):
        return self.nome

class AgendaInstitucinal(AgendaMain):
    nome = models.CharField(max_length = 100)
    empresa = models.ForeignKey(Empresa, related_name = 'Empresa', null = True, blank = False)

    def __str__(self):
        return self.nome
# Create your models here.
