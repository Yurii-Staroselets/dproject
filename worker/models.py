from django.db import models
from shop.models import Shop


class Worker(models.Model):
    full_name = models.CharField(max_length=255, db_index=True)
    position = models.CharField(max_length=255)
    salary = models.CharField(max_length=255)
    shop = models.ForeignKey(Shop, related_name='worker', on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name
# Create your models here.
