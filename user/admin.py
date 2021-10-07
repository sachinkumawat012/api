from django.contrib import admin
from django.contrib.admin.decorators import display
from . models import Post
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    display_list = ['id', 'username', 'image', 'caption']
