# Uncomment the following imports before adding the Model code

from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.


class CarMake(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    founded_year = models.PositiveIntegerField(null=True, blank=True)
    country = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    SEDAN = 'Sedan'
    SUV = 'SUV'
    WAGON = 'Wagon'
    CAR_TYPE_CHOICES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'Wagon'),
    ]

    car_make = models.ForeignKey(
        'CarMake',
        on_delete=models.CASCADE,
        related_name='car_models'
    )
    dealer_id = models.IntegerField()
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=CAR_TYPE_CHOICES)
    year = models.PositiveIntegerField()
    color = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return f"{self.car_make.name} {self.name} ({self.year})"
