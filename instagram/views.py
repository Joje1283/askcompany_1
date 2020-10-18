from django.views.generic import ListView, DetailView
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Post

post_list = ListView.as_view(model=Post)

# def post_list(request):
#     qs = Post.objects.all()
#     q = request.GET.get('q', '')
#     if q:
#         qs = qs.filter(message__icontains=q)  # 5분 5초
#         # instagram/templates/instagram/post_list.html
#     return render(request, 'instagram/post_list.html', {
#         'post_list': qs,
#         'q': q,
#     })


# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'instagram/post_detail.html', {
#         'post': post
#     })

post_detail = DetailView.as_view(model=Post)


def archives_year(request, year):
    return HttpResponse(f"{year}년 archives")
