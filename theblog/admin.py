from django.contrib import admin
from . models import Post, Comment, Reply, Profile#, Category

admin.site.register(Post)
# admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(Profile)
