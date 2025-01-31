from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    year_of_study = models.IntegerField()
    faculty = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} {self.surname} ({self.major}, {self.year_of_study} курс, {self.faculty})"