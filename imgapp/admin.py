from django.contrib import admin

# Register your models here.

from .models import UnprocessedImg
admin.site.register(UnprocessedImg)

from .models import ProcessedImg
admin.site.register(ProcessedImg)