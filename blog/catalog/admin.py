from django.contrib import admin
from .models import Comment, CustomUser, Post, LikePost, LikeComment
# Register your models here.

admin.site.register(Comment)
admin.site.register(CustomUser)
admin.site.register(Post)
admin.site.register(LikePost)
admin.site.register(LikeComment)
