from django.db import models

# Create your models here.
class SignupForm(models.Model):
    username = models.CharField(max_length=30,unique=True)
    email    = models.EmailField(unique=True)
    password = models.CharField(max_length=30)


    class Meta:
        db_table = 'Blog'