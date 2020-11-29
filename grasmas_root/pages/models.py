from django.db import models


class Gift(models.Model):
    giver = models.CharField(max_length=10)
    title = models.CharField(max_length=12)
    desc = models.CharField(max_length=120)
    recvr = models.CharField(max_length=12, blank=True)
    author = models.CharField(max_length=12)
    color = models.CharField(max_length=12)

    # def __str__(self):
    #     return self.title
