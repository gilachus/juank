from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    barcode = models.ImageField(upload_to='images/')

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        pass