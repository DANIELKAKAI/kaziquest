from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    role = models.CharField(max_length=20)
    verified = models.BooleanField(default=False)
    def __str__(self):
        return self.user.username
    class Meta:
        verbose_name_plural="UserProfile"