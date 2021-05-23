from django.db import models

# Create your models here.
class user(models.Model):
    fname = models.CharField(max_length = 255)
    lname = models.CharField(max_length = 255)
    email = models.EmailField(max_length = 255, unique=True)

    def __str__(self):
        return self.email