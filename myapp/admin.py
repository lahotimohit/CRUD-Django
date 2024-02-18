from django.contrib import admin
from . import models

class stadmin(admin.ModelAdmin):
    list_display = ['id','name', 'course']

# Register your models here.
admin.site.register(models.student, stadmin)