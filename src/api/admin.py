from django.contrib import admin
from .models import Category, Task, Profile
# Register your models here.

admin.site.register(Category)
admin.site.register(Task)
admin.site.register(Profile)
