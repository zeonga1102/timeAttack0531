from django.shortcuts import render, redirect
from .models import Category, Article


# Create your views here.
def newView(request):
    if request.method == 'GET':
        category = Category.objects.all()
        return render(request, 'new.html', {'category': category})
    elif request.method == 'POST':
        title = request.POST.get('title', '')
        content = request.POST.get('desc', '')
        categoryName = request.POST.get('category', '')
        category = Category.objects.get(name=categoryName)

        article = Article.objects.create(title=title, content=content, category=category)
        article.save()

        return redirect(f'/detail/{article.id}')


def categoryView(request):
    category = Category.objects.all()
    info = {}
    for c in category:
        info[c.name] = Article.objects.filter(category=c).count()
    return render(request, 'category.html', {'info': info})


def articleView(request, category):
    categoryObject = Category.objects.get(name=category)
    article = Article.objects.filter(category=categoryObject)
    return render(request, 'article.html', {'article': article})

def detailView(request, id):
    article = Article.objects.get(id=id)
    return render(request, 'detail.html', {'article': article})

