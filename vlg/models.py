from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100)
    text = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    class Met:
        ordering=["-date_creation"]

    def __str__(self):
        return self.title

class Comment(models.Model):
    text = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post)
    user=models.ForeignKey(User)

    def __str__(self):
        return self.text[0:20]

    def get_nubmer_of_comments(self):
        return self.count-self[1]