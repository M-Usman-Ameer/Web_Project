from django.db import models
from autoslug import AutoSlugField

class Postblog(models.Model):
    Tital = models.CharField(max_length=150)
    contant = models.TextField(max_length=300)
    slug = AutoSlugField(populate_from='Tital', unique=True, null=True, default=0)


    def __str__(self):
        return self.Tital

