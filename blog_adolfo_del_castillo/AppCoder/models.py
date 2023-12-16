from django.db import models

class Usuario(models.Model):
    nombreUsuario = models.CharField(max_length=15)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
   

    def __str__(self):
        return f"nombreUsuario: {self.nombreUsuario}, nombre: {self.nombre}, apellido: {self.apellido}, email: {self.email}"

class Publicacion(models.Model):
    nombreUsuario = models.CharField(max_length=15)
    titulo = models.CharField(max_length=50)
    comentario = models.CharField(max_length=200)
    fecha = models.DateField()

class Comentarios(models.Model):
    idPublicacion = models.IntegerField()
    nombreUsuario = models.CharField(max_length=15)
    comentario = models.CharField(max_length=200)
    fecha = models.DateField() 