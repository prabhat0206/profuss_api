from django.db import models

# Create your models here.

class Product(models.Model):
    id=models.AutoField(primary_key=True)
    product_name=models.CharField(max_length=255)
    category=models.CharField(max_length=255)
    price=models.IntegerField()
    image=models.ImageField(upload_to="")
    description=models.TextField()
    offer=models.IntegerField()
    category_id=models.IntegerField()
