from django.db import models

class allcourses(models.Model):
    coursename=models.CharField(max_length=200)
    insname=models.CharField(max_length=200)

    def __str__(self):
        return self.coursename
        return self.insname

class details(models.Model):
    course=models.ForeignKey(allcourses, on_delete=models.CASCADE)
    sp=models.CharField(max_length=500)
    il=models.CharField(max_length=500)

    def __str__(self):
        return self.pk

# Create your models here.
