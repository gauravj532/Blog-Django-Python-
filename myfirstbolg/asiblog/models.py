from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
	
    title = models.CharField(max_length=200)
    body = models.TextField()
     
    publish = models.BooleanField(default=True)          #for soft delete
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)      # see what to do
    user = models.ForeignKey(User,default= )

    def __unicode__(self):
        return '%s' % self.title
    
class Tag(models.Model):
    slug = models.SlugField(max_length=200)
    post = models.ManyToManyField(Post)
