from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view , name='home'),
    path('Service', views.service_view , name='service'),
    path('About_us' , views.about_view, name='about'),
    path('Contact', views.ContactMessage_view, name='Contact'),
    path('register',views.register_view, name='register'),
    path('login',views.login_view, name='login'),
    path('logout',views.logout_view, name='logout'),
    path('UK',views.UK_view , name='UK'),
    path('USA',views.USA_view , name='USA'),
    path('Italy',views.canada_view , name='italy'),
    path('Austrial',views.austrila_view , name='austrila'),
    path('Admission Form',views.Admissionform,name='Admissionfrom')
]
