from django.shortcuts import render, redirect
from .models import NewsPost
from .forms import NewsPostForm
from django.contrib.auth.decorators import login_required

def news_list(request):
    posts = NewsPost.objects.all()
    return render(request, 'news/news_list.html', {'posts': posts})

def news_detail(request, pk):
    post = NewsPost.objects.get(pk=pk)
    return render(request, 'news/news_detail.html', {'post': post})

@login_required
def add_news(request):
    if request.method == 'POST':
        form = NewsPostForm(request.POST, request.FILES)
        if form.is_valid():
            news = form.save(commit=False)
            news.author = request.user
            news.save()
            return redirect('news:news_list')
    else:
        form = NewsPostForm()
    return render(request, 'news/add_news.html', {'form': form})
