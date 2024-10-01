from django.db import models
from cloudinary.models import CloudinaryField
from django.urls import reverse

# Create your models here.

class Share(models.Model):
    """
    Stores a share art  entered by a user related to :model:`auth.User`.
    """
    name = models.CharField(max_length=50)
    picture = CloudinaryField('image', default='placeholder')
    title = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
       
        return reverse('share')