from django.db import models

# Create your models here.

class Category(models.Model):
    description  = models.CharField(max_length=100)

    def __str__(self):
        return self.description
    
class Publisher(models.Model):
    name = models.CharField(max_length=100)
    site = models.URLField(null=True, blank=True)
    
    def __str__(self):
        return self.name