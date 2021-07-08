from django.db import models


class student(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone_no = models.IntegerField()
    city = models.CharField(max_length=200)


class books(models.Model):
    stu = models.ForeignKey(student, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.IntegerField()
