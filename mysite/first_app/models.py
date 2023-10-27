from django.db import models

class Employee(models.Model):
    EmpId = models.CharField(max_length=255)
    EmpName = models.CharField(max_length=255)
    EmpGender = models.CharField(max_length=255)
    EmpEmail = models.EmailField()
    EmpDesignation = models.CharField(max_length=255)
    class Meta:
        db_table="Employee"