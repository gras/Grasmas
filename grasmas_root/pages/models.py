from django.db import models


class Gift(models.Model):
    giver = models.CharField(max_length=12)
    title = models.CharField(max_length=30)
    desc = models.CharField(max_length=120)
    recvr = models.CharField(max_length=12, blank=True)
    author = models.CharField(max_length=12)
    color = models.CharField(max_length=12)
    photo = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.giver
