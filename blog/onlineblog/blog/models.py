from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.db.models.fields import CharField, TextField

# Create your models here.
class Post(models.Model):
    author = models.CharField(max_length=128)
    title = models.CharField(max_length=256)
    text = models.TextField()
    published_date = models.DateField(default=timezone.now())

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.title
    