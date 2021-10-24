from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_name = models.CharField(max_length=50)
    post_cat = models.CharField(max_length=50)
    post_pub_date = models.DateField(auto_now_add=True)