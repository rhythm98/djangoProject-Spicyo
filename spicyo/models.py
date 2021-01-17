from django.db import models

# Create your models here.

class Dish(models.Model):
    # id: int  <--not needed since postgreSql will take care of it
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)