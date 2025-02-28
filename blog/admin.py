from django.contrib import admin
from blog.models import Tag, Post

# Registrar Tag con configuración predeterminada
admin.site.register(Tag)

# Configurar Post en el admin
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('slug', 'published_at')

# Registrar Post con la configuración personalizada
admin.site.register(Post, PostAdmin)
