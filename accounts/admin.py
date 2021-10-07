from django.contrib import admin
from .models import Profile
# Register your models here.
@admin.register(Profile)
class Profiles(admin.ModelAdmin):
    display_list = ['id', 'image', 'caption']