from django.contrib import admin
from .models import Category, Post
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated') #Campos de solo lectura
    list_display = ('title','author','published', 'post_categories') #Columnas que sean visibles
    ordering = ('author', 'published') #Ordenar las columnas
    search_fields = ('title','content','author__username','categories__name') #Crea una barra de buscador y busca los elementos que uno agrega
    date_hierarchy =  'published'#Sirve para filtrar por fechas
    list_filter =('author__username', 'categories__name')#Otro filtro mas

    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])

    post_categories.short_description = "Categorias" #Cambiamos el nombre de post_categories que se encuentra en list_display

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
