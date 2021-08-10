from django.contrib import admin
from .models import Post, BlogComment

# model registering
admin.site.register((Post, BlogComment))
