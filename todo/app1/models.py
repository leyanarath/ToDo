from django.db import models

# Create your models here.
class Task(models.Model):
    name=models.CharField(max_length=100)
    priority=models.IntegerField()
    date = models.DateField()
    def __str__(self):
        return self.name

# class emp(models.Model):
#     firstname=models.CharField(max_length=20)
#     lastname=models.CharField(max_length=20)
#     age=
