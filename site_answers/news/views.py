from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm

def news(request):
    news = Articles.objects.order_by('title')
    return render(request, 'news/news.html', {'news': news})

def create(request):
    error = ""
    if request.method == "POST":
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news')
        else:
            error = "Ошибка"
    form = ArticlesForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)