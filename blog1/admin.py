from django.contrib import admin
from blog1.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass
