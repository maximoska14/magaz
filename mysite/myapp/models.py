from django.db import models

class zap(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    number_det = models.CharField(max_length=100)
    number_kuz = models.CharField(max_length=100)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name
