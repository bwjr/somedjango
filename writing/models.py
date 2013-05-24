from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length = 500)
    email = models.EmailField()
    password = models.CharField(max_length = 500)
    created_date = models.DateField(auto_now_add = True)

    def __unicode__(self):
        return self.name

class Paper(models.Model):
    title = models.CharField(max_length = 1000)
    body = models.TextField()
    time = models.DateTimeField(auto_now = True)

    def __unicode__(self):
        return self.title

class Comments(models.Model):
    thepaper = models.ForeignKey(Paper)
    by_user = models.ForeignKey(User)
    comment = models.TextField()
    upvotes = models.IntegerField(default = 0)
    downvotes = models.IntegerField(default = 0)

    def __unicode__(self):
        return self.comment
