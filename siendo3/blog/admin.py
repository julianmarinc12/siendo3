from django.contrib import admin
from .models import Categoria,Post

# Register your models here.

class CAtegoriaAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

class PostaAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Categoria,CAtegoriaAdmin)
admin.site.register(Post,PostaAdmin)