from django.db import models
from django.conf import settings

# Create your models here.
class Products(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=300)
    author=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='products')
    wish=models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='wish')
    hits=models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='hits')
    image=models.ImageField(upload_to='images/', blank=True)
    created_at=models.DateTimeField(auto_now_add=True)