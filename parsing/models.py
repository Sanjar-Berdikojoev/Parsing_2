from django.db import models

class Goods(models.Model):
    title = models.CharField(max_length=100)
    title_text = models.CharField(max_length=100)
    image = models.ImageField(upload_to='')
    price = models.CharField(max_length=100)

    def __str__(self):
        return self.title



# Create your models here.
