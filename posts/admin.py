"""Post admin clases."""

#Django
from django.contrib import admin

#Models
from .models import Post

admin.site.register(Post)