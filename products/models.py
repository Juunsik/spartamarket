from django.db import models
from django.conf import settings

# Create your models here.
class Product(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=300)
    author=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='products')
    wish=models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='wish', blank=True)
    hits=models.PositiveIntegerField(default=0)
    image=models.ImageField(upload_to='images/')
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title