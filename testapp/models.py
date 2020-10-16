from django.db import models

class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')
    time = models.CharField(max_length=200, default="Not downloaded yet")
    downloaded = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title