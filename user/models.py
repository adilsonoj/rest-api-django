from django.db import models

# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=30)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=100)
    role = models.ForeignKey(Role, on_delete=models.DO_NOTHING)
    created_at = models.DateField()

    def __str__(self):
        return self.name
