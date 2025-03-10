from django.db import models
from Admin.models import *
from Guest.models import *

class tbl_candidate(models.Model):
    candidate_name=models.CharField(max_length=50) 
    candidate_email=models.CharField(max_length=50) 
    candidate_password=models.CharField(max_length=50)

class tbl_examination(models.Model):
    examination_name=models.CharField(max_length=50) 
    examination_mark=models.CharField(max_length=50) 
    examination_qno=models.CharField(max_length=50) 
    examination_time=models.CharField(max_length=50) 
    examination_status = models.IntegerField(default=0)
    time = models.TimeField(null=True)
    start_time = models.TimeField(null=True)
    cordinator=models.ForeignKey(tbl_cordinator,on_delete=models.CASCADE,null=True)

class tbl_questions(models.Model):
    question=models.CharField(max_length=100) 
    examination=models.ForeignKey(tbl_examination,on_delete=models.CASCADE)

class tbl_options(models.Model):
    questions=models.ForeignKey(tbl_questions,on_delete=models.CASCADE)
    answer=models.CharField(max_length=100)
    status = models.BooleanField() 





    

# Create your models here.
