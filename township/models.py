from django.db import models


# Create your models here.

class State(models.Model):
    STATE_NUMBER = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
        ('13', '13'),
        ('14', '14'),
    )
    state_name = models.CharField(max_length=50)
    number = models.CharField(max_length=2, choices=STATE_NUMBER)

    def __str__(self):
        return self.state_name


class Township(models.Model):
    name = models.CharField(max_length=50)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
