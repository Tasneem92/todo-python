from django.contrib import admin
from . models import Todo, TodoMirror

# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    search_fields = ('name','description')
    ordering = ['id']
admin.site.register(Todo, TodoAdmin)


class TodoMirrorAdmin(admin.ModelAdmin):
    search_fields = ('name','description')
    ordering = ['id']
admin.site.register(TodoMirror, TodoMirrorAdmin)
