from django.db import models

class Pet(models.Model):
    #class variables
    SEX_CHOICES = [('M', 'Male'),('F', 'Female')]


    name = models.CharField(max_length=100)
    submitter = models.CharField(max_length=100)
    species = models.CharField(max_length=50)
    breed = models.CharField(max_length=50, blank=True) #some animals might not be a pure breed. Allow blank=true
    description = models.TextField()
    sex = models.CharField(choices=SEX_CHOICES, max_length=1)
    submission_date = models.DateTimeField()
    age = models.IntegerField(null=True) #pets rescued can be of an unknown age, use null to distinguish from age 0
    vaccinations = models.ManyToManyField('Vaccine', blank=True) #many pets can have the same vaccine, each pet can have many vaccines

class Vaccine(models.Model):
    name = models.CharField(max_length=50)

    