from django.db import models


class Post(models.Model):
    message = models.TextField()
    photo = models.ImageField(blank=True, upload_to='instagram/post/%Y/%m/%d')  # Pillow 설치해야 함.
    is_public = models.BooleanField(default=False, verbose_name='공개여부')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Java의 toString
    def __str__(self):
        # return f'Post Object({self.id})'
        return self.message

    class Meta:
        ordering = ['-id']  # 내림차순 정렬
        # 쿼리에서 Post.objects.all()[::2]와 같이 슬라이싱이 반영될 경우, lazy한 속성이 사라짐(바로 쿼리 실행)

    '''
    def message_length(self):  # 인자 없는 함수만 admin에서의 필드로서의 사용이 가능함
        return len(self.message)
    message_length.short_description = '메시지 글자 수'
    '''
