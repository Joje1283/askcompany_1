from django.db import models


class Post(models.Model):
    message = models.TextField()
    is_public = models.BooleanField(default=False, verbose_name='공개여부')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Java의 toString
    def __str__(self):
        # return f'Post Object({self.id})'
        return self.message

    '''
    def message_length(self):  # 인자 없는 함수만 admin에서의 필드로서의 사용이 가능함
        return len(self.message)
    message_length.short_description = '메시지 글자 수'
    '''
