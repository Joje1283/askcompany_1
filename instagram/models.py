from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


# class User(AbstractUser):
#     pass

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
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


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, # post_id 필드가 생성이 됩니다.
                             limit_choices_to={'is_public': True})
    # limit_choices_to={'is_public': True} 옵션 -> Post의 is_public이 True인 로우만 어드민 or 장고 Form 에서 노출한다.
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
