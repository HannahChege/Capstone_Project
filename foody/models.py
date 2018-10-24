from django.db import models

# Create your models here.
class Image(models.Model):
    food = models.CharField(max_length =30)
    image = models.ImageField(upload_to = 'photos/', default='No image')
    price = models.CharField(max_length =15)

    def save_image(self):
        self.save()
    def delete_image(self):
        self.delete()

    def __str__(self):
        return self.food   
    classmethod
    def get_all_images(cls):
        all_images = Image.objects.all()
        return all_images
    
    @classmethod
    def get_image_by_id(cls, id):
        an_image = Image.objects.get(id=id)
        return an_image    

# class Restratuant(models.Model):
#     name = models.CharField(max_length =30)
#     location= models.CharField(max_length =30)
#     food = models.ManyToManyField(food)

   
#     def __str__(self):
#         return self.name
#     def save_restratuant(self):
#         self.save()  

#     def delete_restratuant(self):
#         self.delete()  

#     @classmethod
#     def update_restratuant(cls,update):
#         pass
     
    