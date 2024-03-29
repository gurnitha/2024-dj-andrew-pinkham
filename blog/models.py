# blog/models.py

from django.db import models

# Model Field Reference
# https://docs.djangoproject.com/en/5.0/ref/models/fields/

from organizer.models import Tag, Startup

class Post(models.Model):
    title = models.CharField(max_length=63)
    slug = models.SlugField()
    text = models.TextField()
    pub_date = models.DateField()
    tags = models.ManyToManyField(Tag)
    startups = models.ManyToManyField(Startup)