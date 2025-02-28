from django.db import models  # Importamos el módulo models de Django para definir modelos de base de datos
from django.conf import settings  # Importamos settings para obtener el modelo de usuario configurado en Django

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
    created_at = models.DateTimeField(auto_now_add=True)  # Se establece automáticamente al crear el post
    modified_at = models.DateTimeField(auto_now=True)  # Se actualiza cada vez que se modifica el post
    
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

    def __str__(self):
        return self.title  # Retorna el título como representación en string del objeto Post
