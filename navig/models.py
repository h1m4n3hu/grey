from django.db import models

# Create your models here.
class Socket(models.Model):
    numb=models.IntegerField(default=0)
    vid=models.CharField(max_length=500,default=0)
    name1=models.CharField(max_length=10,default=0)
    file1=models.CharField(max_length=10000,default=0)
    name2=models.CharField(max_length=10,default=0)
    file2=models.CharField(max_length=10000,default=0)
    def __str__(self):
        return str(self.numb)

class Gitandvsc(models.Model):
    numb=models.IntegerField(default=0)
    vid=models.CharField(max_length=500,default=0)
    name1=models.CharField(max_length=10,default=0)
    file1=models.CharField(max_length=10000,default=0)
    def __str__(self):
        return str(self.numb)

class Pygame(models.Model):
    numb=models.IntegerField(default=0)
    vid=models.CharField(max_length=500,default=0)
    name1=models.CharField(max_length=10,default=0)
    file1=models.CharField(max_length=10000,default=0)
    def __str__(self):
        return str(self.numb)

class Submission(models.Model):
    ied=models.CharField(max_length=100)
    option=models.CharField(max_length=50)
    date=models.CharField(max_length=50)
    did=models.CharField(max_length=4)
    def __str__(self):
        return str(self.date+self.did)