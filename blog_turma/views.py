from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone
#O ponto antes do models significa diretório atual, antes eu escrevia from blog_turma.models import Post.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') 
    return render(request, 'blog_turma/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog_turma/post_detail.html', {'post': post})