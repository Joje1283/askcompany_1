from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'message', 'message_length', 'is_public', 'created_at', 'updated_at')
    list_display_links = ('message',)
    search_fields = ('message',)
    list_filter = ('created_at', 'is_public')

    def message_length(self, post):
        return f'{len(post.message)} 글자'
    message_length.short_description = '메시지 글자 수'