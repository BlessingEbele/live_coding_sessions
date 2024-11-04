from django.db import models

# Create your models here.
class student(models.Model):
    first_name=models.CharField(max_lenght=10)
    lastname=models.CharField(max_lenght=5)
    adress =models.CharField(max_lenght=20)
    bio =models.CharField(max_lenght=20)
    is_validated =models.BooleanField(dafualt=True)
    created =models.DateTimeField(auto_now_add=True)