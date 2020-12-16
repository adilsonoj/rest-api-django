from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateField()

    def __str__(self):
        return self.name