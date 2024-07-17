from django.db import models

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    population = models.IntegerField()

    def __str__(self):
        return self.name

class Attraction(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    opening_hours = models.CharField(max_length=50)
    city = models.ForeignKey(City, related_name='attractions', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Review(models.Model):
    rating = models.IntegerField()
    comment = models.TextField()
    date_posted = models.DateField(auto_now_add=True)
    attraction = models.ForeignKey(Attraction, related_name='reviews', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.rating} - {self.attraction.name}"
