from django.db import models
from django.contrib.auth.models import User

class Paper(models.Model):
    by_user = models.OneToOneField(User)
    title = models.CharField(max_length = 1000)
    body = models.TextField()
    time = models.DateTimeField(auto_now = True)

    def __unicode__(self):
        return self.title

class Comments(models.Model):
    thepaper = models.ForeignKey(Paper)
    by_user = models.OneToOneField(User)
    comment = models.TextField()
    upvotes = models.IntegerField(default = 0)
    downvotes = models.IntegerField(default = 0)

    def __unicode__(self):
        return self.comment
