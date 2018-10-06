from django.db import models


# Create your models here.
class Judge(models.Model):
    # This table will hold the info for each judge
    first_name      = models.CharField(max_length=250)
    last_name       = models.CharField(max_length=250)
    user_name       = models.CharField(max_length=250)
    password        = models.CharField(max_length=250)

    def __str__(self):
        return '%s' % (self.name)

    class Meta:
        verbose_name_plural = "Judges"


class JudgeGroup(models.Model):
    name    = models.CharField(max_length=250)
    user    = models.ForeignKey(Judge, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % (self.name)

    class Meta:
        verbose_name_plural = "Judge groups"
