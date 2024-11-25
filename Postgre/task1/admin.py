from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Task1User)
class AdminUser(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name',)
