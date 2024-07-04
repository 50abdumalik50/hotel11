from django.contrib import admin
from apps.news.models import Post, PostImage, Comment

admin.site.register(Post)
admin.site.register(PostImage)
admin.site.register(Comment)
