from django.contrib import admin
from .models import Postblog

class Postadmin(admin.ModelAdmin):
    list_display = ['Tital','slug','contant']
    prepopulated_fields = {'slug': ('Tital',)}
admin.site.register(Postblog,Postadmin)