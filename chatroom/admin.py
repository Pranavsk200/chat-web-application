from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Users),
admin.site.register(messages),
admin.site.register(Room),
admin.site.register(relationship),
admin.site.register(Friends)