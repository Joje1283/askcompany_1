from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Post

# post_list = login_required(ListView.as_view(model=Post, paginate_by=10))


# @method_decorator(login_required, name='dispatch')
class PostListView(LoginRequiredMixin, ListView):
    model = Post
    paginate_by = 10


post_list = PostListView.as_view()

# @login_required
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

# post_detail = DetailView.as_view(
#     model=Post,
#     queryset=Post.objects.filter(is_public=True))


class PostDetailView(DetailView):
    model = Post

    def get_queryset(self):
        qs = super().get_queryset()
        print(not self.request.user.is_authenticated)
        if not self.request.user.is_authenticated:
            qs = qs.filter(is_public=True)
        return qs


post_detail = PostDetailView.as_view()


def archives_year(request, year):
    return HttpResponse(f"{year}년 archives")
