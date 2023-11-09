from time import strftime

from django.db import models


# Create your models here.
class Site(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Unit(models.Model):
    name = models.CharField(max_length=25)
    symbol = models.CharField(max_length=5)

    def __str__(self):
        return self.name


class Equipment(models.Model):
    name = models.CharField(max_length=100)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

equipment = Equipment()
equipment.name
equipments = .....filter()

class Measure(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    value = models.FloatField()

    def __str__(self):
        return self.equipment.name + " || " + self.datetime.astimezone().__str__() + " || " + str(self.value)