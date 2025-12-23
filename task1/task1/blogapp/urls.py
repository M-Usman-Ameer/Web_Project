from django.contrib import admin
from django.urls import path
from blogapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home , name='home'),
    path('post/<slug:slug>/',views.post , name='post')
]