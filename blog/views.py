from django.shortcuts import render, redirect
from .models import Category, Article


# Create your views here.
def showNew(request):
    if request.method == 'GET':
        category = Category.objects.all()
        return render(request, 'new.html', {'category': category})
    elif request.method == 'POST':
        title = request.POST.get('title', '')
        content = request.POST.get('content', '')
        category = request.POST.get('category', '')

        article = Article.objects.create(title=title, content=content, category=category)
        article.save()

        return redirect(f'/{category}/{article.id}')


def showCategory(request):
    category = Category.objects.all()
    return render(request, 'category.html', {'category': category})


def showArticleList(request, category):
    article = Article.objects.filter(category=category)
    return render(request, 'article.html', {'article': article})

