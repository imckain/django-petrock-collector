from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner'),
)

class Hat(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("hats_detail", kwargs={"pk": self.id})

class Petrock(models.Model):
    name = models.CharField(max_length=250)
    rockType = models.CharField(max_length=250)
    description = models.TextField(max_length=250)
    personality = models.IntegerField()
    hats = models.ManyToManyField(Hat)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("petrocks_detail", kwargs={"petrock_id": self.id})

    def fed_for_today(self):
        return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)

class Feeding(models.Model):
    date = models.DateField('feeding date')
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0]
    )
    petrock = models.ForeignKey(Petrock, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"

    class Meta:
        ordering = ['-date']

class Photo(models.Model):
    url = models.CharField(max_length=200)
    petrock = models.ForeignKey(Petrock, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for petrock id#{self.petrock_id} @ {self.url}"
