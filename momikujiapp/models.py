from django.db import models

# Create your models here.

class MomikujiModel(models.Model):
    text = models.CharField(max_length=100)

    def __str__(self):
        return self.text