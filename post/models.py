from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse



class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE )
    title = models.CharField(max_length=200)
    content = models.TextField()
    picture = models.FileField(blank=True , null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    def delete_from_page(self):

        self.is_deleted = not self.is_deleted
        self.save()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
    
      return reverse("post_detail", kwargs={ "id" : self.pk } )
    