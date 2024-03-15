from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#one to one cardinality 
class Page(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    page_name=models.CharField(max_length=100)
    page_cat=models.CharField(max_length=100)
    page_publish=models.DateField()

#one to many or many to one cadinality
class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    post_title=models.CharField(max_length=100)
    post_cat=models.CharField(max_length=100)
    post_publish_date=models.DateField()


#many to many cardinalities...
class Song(models.Model):
    user=models.ManyToManyField(User)
    title=models.CharField(max_length=50)
    artist=models.CharField(max_length=50)

    def customuser(self):
            return ','.join([str(p) for p in self.user.all()])

# def writtenby(self):
#     return ','.join([str(p) for p in self.user.all()])