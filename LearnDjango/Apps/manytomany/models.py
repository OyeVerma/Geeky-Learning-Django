from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Song(models.Model):
    user = models.ManyToManyField(User)
    song_name = models.CharField(max_length=50)
    song_duration = models.IntegerField()

    def written_by(self):
        return ",".join([str(us) for us in self.user.all()])