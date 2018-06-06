from django.db import models

# Create your models here.
class Thing(models.Model):
    # it's name is a character field up to 255
    name = models.CharField(max_length = 255)
    # a text field describes it
    description = models.TextField()
    slug = models.SlugField(unique = True)
