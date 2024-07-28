from django.http import HttpResponse
from django.shortcuts import render
from posts.models import Post


def post1_view(request):
    return HttpResponse("Путь по этой ссылке возвращает текстовый ответ.")


def post2_view(request):
    posts = Post.objects.all()
    return HttpResponse(posts)


def post3_view(request):
    posts = Post.objects.all()
    return render(request=request, template_name='post3_view.html', context={'posts': posts})


def post_detail_view(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'post_detail_view.html', {'post': post})

def main_page(request):
    return render(request=request, template_name='index.html')
