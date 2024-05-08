from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=50)
    roll_number = models.IntegerField()
    age = models.IntegerField()
    mark = models.IntegerField()

    def __str__(self):
        return self.name