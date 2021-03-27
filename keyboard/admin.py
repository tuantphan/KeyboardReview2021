from django.contrib import admin
from .models import KeyboardName, KeyboardType, KeyboardReview
# Register your models here.
admin.site.register(KeyboardName)
admin.site.register(KeyboardType)
admin.site.register(KeyboardReview)