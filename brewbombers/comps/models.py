from django.db import models


# Create your models here.
class JudgeGroup(models.Model):
    name    = models.CharField(max_length=250)

    def __str__(self):
        return '%s' % (self.name)

    class Meta:
        verbose_name_plural = "Judge groups"


class Judge(models.Model):
    # This table will hold the info for each judge
    first_name      = models.CharField(max_length=250)
    last_name       = models.CharField(max_length=250)
    judge_group     = models.ForeignKey(JudgeGroup, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % (self.name)

    class Meta:
        verbose_name_plural = "Judges"
