from django.contrib import admin
from .models import JudgeGroup
from .models import Judge


# Register your models here.
admin.site.register(JudgeGroup)
admin.site.register(Judge)
