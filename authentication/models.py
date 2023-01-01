from django.db import models
from PIL import Image

# Create your models here.
class ImageModel(models.Model):
    photo = models.ImageField(upload_to="myimage")
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs): 
        super().save(*args, **kwargs)
        img = Image.open(self.photo.path) 
        output_size = (200,300) 
        img.thumbnail(output_size)
        img.save(self.photo.path)
