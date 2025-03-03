from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from django.utils import timezone


# Modelo de Comentario con relación genérica
class Comment(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    # Relación genérica
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")
    # Fechas de creación y modificación
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.creator} on {self.content_type} (ID: {self.object_id})"


# Creamos el modelo Tag, que representa etiquetas que pueden asociarse a los posts del blog
class Tag(models.Model):
    value = models.TextField(max_length=100)  # Campo de texto para almacenar el nombre de la etiqueta

    def __str__(self):
        return self.value  # Retorna el valor de la etiqueta como representación en string

# Creamos el modelo Post, que representa las entradas del blog
class Post(models.Model):
    # Relacionamos cada post con un autor (usuario del sistema)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    # Fechas de creación y modificación automáticas
    #created_at = models.DateTimeField(auto_now_add=True)  # Se establece automáticamente al crear el post
    #modified_at = models.DateTimeField(auto_now=True)  # Se actualiza cada vez que se modifica el post
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    # Fecha opcional de publicación (puede estar vacía)
    published_at = models.DateTimeField(blank=True, null=True)
    # Título del post con un límite de 100 caracteres
    title = models.TextField(max_length=100)
    # Slug: una versión amigable del título para URLs
    slug = models.SlugField()
    # Resumen del post con un límite de 500 caracteres
    summary = models.TextField(max_length=500)
    # Contenido del post, sin restricción de caracteres
    content = models.TextField()
    # Relación ManyToMany con Tag, permitiendo múltiples etiquetas por post
    tags = models.ManyToManyField(Tag, related_name="posts")
    # Relación inversa con Comment
    comments = GenericRelation(Comment)

    def __str__(self):
        return self.title  # Retorna el título como representación en string del objeto Post
