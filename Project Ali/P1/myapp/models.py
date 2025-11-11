from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class WebsiteUser(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    date_joined = models.DateTimeField(auto_now_add=True)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.username


class Apply(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.fullname


    

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    last_qualification = models.CharField(max_length=100)
    percentage_year = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    course_interest = models.CharField(max_length=150)
    english_test = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
