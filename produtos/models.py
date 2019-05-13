from django.db import models


# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    photo = models.ImageField(upload_to='products_photos', null=True, blank=True)

    def __str__(self):
        return self.name
