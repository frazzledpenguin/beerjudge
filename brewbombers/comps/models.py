from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class JudgeGroup(models.Model):
    name    = models.CharField(max_length=250)
    user    = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % (self.name)

    class Meta:
        verbose_name_plural = "Judge groups"
