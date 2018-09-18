from django.contrib import admin
from .models import Judge_group
from .models import Judge


# Register your models here.
admin.site.register(Judge_group)
admin.site.register(Judge)
