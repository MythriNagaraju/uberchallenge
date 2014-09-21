from django.db import models

class FoodFacility(models.Model):
    locationid = models.IntegerField()
    Applicant = models.CharField(max_length = 1000)
    FacilityType = models.CharField(max_length = 100)
    cnn = models.IntegerField()
    LocationDescription = models.CharField(max_length = 1000)
    blocklot = models.CharField(max_length = 1000)
    block = models.CharField(max_length = 1000)
    lot = models.CharField(max_length = 1000)
    permit = models.CharField(max_length = 1000)
    Address = models.CharField(max_length = 1000)
    Status = models.CharField(max_length = 1000)
    FoodItems = models.CharField(max_length = 1000)
    X = models.FloatField()
    Y = models.FloatField()
    Latitude = models.FloatField()
    Longitude = models.FloatField()
    Schedule = models.CharField(max_length = 1000)
    NOISent = models.CharField(max_length = 1000)
    Approved = models.CharField(max_length = 1000)
    Received = models.CharField(max_length = 1000)
    PriorPermit = models.IntegerField()
    ExpirationDate = models.CharField(max_length=1000)
    Location = models.CharField(max_length=2000)
    
    
