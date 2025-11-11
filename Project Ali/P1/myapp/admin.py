from django.contrib import admin
from .models import  Apply,WebsiteUser,ContactMessage



class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','last_qualification','percentage_year','location','course_interest','english_test','created_at')

class ApplyAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'email','phone','city', 'country')

@admin.register(WebsiteUser)
class WebsiteUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'date_joined')
    search_fields = ('username', 'email')
    ordering = ('-date_joined',)
 

admin.site.register(Apply)
admin.site.register(ContactMessage)


