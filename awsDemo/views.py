from django.shortcuts import render
from .models import Article


def create_article(request):

    if request.GET:
        name = request.GET.get('name')
        title = request.GET.get('title')
        article = Article.objects.create(
            name=name,
            title=title
        )
        article.save()
        article = Article.objects.all()
        context = {
            "article": article
        }
        return render(request, 'homepage/list.html', context)
    return render(request, 'homepage/list.html')
