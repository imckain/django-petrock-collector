from django.db import models
from django.urls import reverse

# Create your models here.
class Petrock(models.Model):
    name = models.CharField(max_length=250)
    rockType = models.CharField(max_length=250)
    description = models.TextField(max_length=250)
    personality = models.IntegerField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("petrocks_detail", kwargs={"petrock_id": self.id})

class Hat(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("hats_detail", kwargs={"pk": self.id})


    