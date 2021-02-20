from django.contrib import admin
from .models import Petrock, Feeding, Hat

# Register your models here.
admin.site.register(Petrock)
admin.site.register(Feeding)
admin.site.register(Hat)