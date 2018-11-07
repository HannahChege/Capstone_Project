from django.db import models
from django.contrib.gis.db.models import PointField
from django.contrib.gis.geos import Point
from django.contrib.gis.db import models

# Create your models here.
class food(models.Model):
    name = models.CharField(max_length =30)
    image = models.ImageField(upload_to = 'photos/', default='No image')
    price = models.CharField(max_length =15)

    def save_food(self):
        self.save()
    def delete_food(self):
        self.delete()

    def __str__(self):
        return self.name  
    classmethod
    def get_all_images(cls):
        all_images = Image.objects.all()
        return all_images
    
    @classmethod
    def get_image_by_id(cls, id):
        an_image = Image.objects.get(id=id)
        return an_image    

class Restaurant(models.Model):
    name = models.CharField(max_length =30)
    location = models.CharField(max_length =30)
    point = models.PointField(default=Point(-1.2921, 36.8219))
    food = models.ManyToManyField(food, related_name="restaurant")
   
    def __str__(self):
        return self.name
    def save_restaurant(self):
        self.save()  

    def delete_restaurant(self):
        self.delete()  

    @classmethod
    def update_restaurant(cls,update):
        pass
class Subscribe(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()
