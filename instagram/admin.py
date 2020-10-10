from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'photo_tag', 'message', 'message_length', 'is_public', 'created_at', 'updated_at')
    list_display_links = ('message',)
    search_fields = ('message',)
    list_filter = ('created_at', 'is_public')

    def photo_tag(self, post):
        if post.photo:
            return mark_safe(f'<img src="{post.photo.url}" style="width: 72px;" />')
        return None

    def message_length(self, post):
        return f'{len(post.message)} 글자'
    message_length.short_description = '메시지 글자 수'
