from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.IntegerField()
    name = models.CharField(max_length=64)

class Module(models.Model):
    module_code = models.CharField(max_length=18)
    name = models.CharField(max_length=64)
    section_id = models.CharField(max_length=3)

class Session(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    date = models.DateField()

class ClassParticipation(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    score = models.IntegerField()