from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True

class Treino(BaseModel):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    duracao = models.IntegerField()

    def __str__(self):
        return self.nome

class Dieta(BaseModel):  # Herda de BaseModel
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    calorias = models.IntegerField()

    def __str__(self):
        return self.nome
    
class Plano(BaseModel):  # Herda de BaseModel
    nome = models.CharField(max_length=100)
    treinos = models.ManyToManyField(Treino)  # Relação muitos-para-muitos com Treino
    dietas = models.ManyToManyField(Dieta)    # Relação muitos-para-muitos com Dieta

    def __str__(self):
        return self.nome    
