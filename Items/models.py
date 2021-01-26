from django.db import models

# Create your models here.


class items(models.Model):
    itemname = models.CharField(max_length=255)
    itemprice = models.FloatField(max_length=255)
    itemimage = models.ImageField(max_length=255, null=True)

    def __str__(self):
        return self.itemname
