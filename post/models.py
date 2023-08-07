from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse
from slugify import slugify
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE )
    title = models.CharField(max_length=200)
    content = models.TextField()
    picture = models.FileField(blank=True , null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
    
      return reverse("post_detail", kwargs={ "id" : self.pk } )
    