from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class blog(models.Model):
    caption=models.TextField(max_length=200)
    pic=models.FileField(upload_to='images', blank=True,null=True)
    username = models.ForeignKey(User, blank=True, null=True)

    def __unicode__(self):
        return self.caption

