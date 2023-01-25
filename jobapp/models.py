from django.db import models

# Create your models here.
class regismodel(models.Model):
    cmp_name=models.CharField(max_length=25)
    address=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.IntegerField()
    password=models.CharField(max_length=20)



class jobmodels(models.Model):
    jobtype = [
        ('Part Time', 'Part Time'),
        ('Full Time', 'Full Time'),

    ]
    worktype=[
        ('Hybrid','Hybrid'),
        ('Remote','Remote'),
    ]
    exptype=[
        ('0-1','0-1'),
        ('1-2','1-2'),
        ('2-3','2-3'),
        ('3-4','3-4'),
        ('4-5','4-5'),
        ('5-6','5-6'),
        ('6-7','6-7'),
        ('7-8','7-8'),
        ('8-9','8-9'),
        ('9-10','9-10'),
    ]

    cmp_name = models.CharField(max_length=50)
    cmp_email = models.EmailField()
    title = models.CharField(max_length=100)
    jobtype = models.CharField(max_length=25,choices=jobtype)
    wrktype = models.CharField(max_length=20,choices=worktype)
    exp_required = models.CharField(max_length=20,choices=exptype)
    qualification = models.CharField(max_length=20)

