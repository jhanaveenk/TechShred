from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Writer)
# admin.site.register(models.Blog)

@admin.register(models.Blog)
class Blogadmin(admin.ModelAdmin):
   list_display = ('title', 'writer', 'date_of_publish')