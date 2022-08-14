from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre=models.CharField(max_length=10)
    apellido=models.CharField(max_length=10)
    dni=models.IntegerField(unique=True)
    celular=models.IntegerField()
    mail=models.EmailField(max_length=30,null=True,blank=True)
    tallepantalon=models.IntegerField(null=True,blank=True)
    tallezapatos=models.IntegerField(null=True,blank=True)
    
class Vestimenta(models.Model):
    ropa=models.BooleanField(max_length=10)
    zapatos=models.BooleanField(max_length=10)
    pulsera=models.BooleanField(max_length=10)
    