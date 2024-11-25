from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=37)
    description = models.TextField()
    data_create = models.DateTimeField(auto_now_add=True)

class Buyer(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(decimal_places=2, max_digits=8)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Task1User(models.Model):
    name = models.CharField(max_length=20)  # This field type is a guess.
    email = models.EmailField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'task1_user'


class Game(models.Model):
    title = models.CharField(max_length=100)
    cost = models.DecimalField(decimal_places=2, max_digits=8)
    size = models.DecimalField(decimal_places=0, max_digits=8)
    description = models.TextField()
    age_limited = models.BooleanField(db_default=False)

    class Meta:
        managed = False
        db_table = 'task1_game'

    def __str__(self):
        return self.title
