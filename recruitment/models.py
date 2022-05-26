from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userProfile',null=True)
    phone = models.CharField(max_length=256, blank=False, null=False)
    academics = models.ForeignKey('Academics', on_delete=models.CASCADE)
    certifications = models.ForeignKey('Certifications', on_delete=models.CASCADE)
    Experience = models.ForeignKey('Experience', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user
    
    class Meta:
        ordering = ['-pk']

class Academics(models.Model):
    degree=models.CharField(max_length=255, blank=True, null=True)
    kcse= models.CharField(max_length=50, null=True, blank=True)
    kcpe= models.CharField(max_length=50, null=True, blank=True)

    # def __str__(self):
    #     return self.academics.userProfile

class Certifications(models.Model):
    cert_name= models.CharField(max_length=100, null=True, blank=True)
    body= models.CharField(max_length=100, null=True, blank=True)

class Experience(models.Model):
    organization= models.CharField(max_length=100, null=True, blank=True)
    period= models.CharField(max_length=100, null=True, blank=True)
    duties= models.TextField(max_length=500, null=True, blank=True)

