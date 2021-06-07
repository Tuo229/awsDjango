from django.shortcuts import render
from .models import Commande


def create_article(request):

    if request.GET:
        name = request.GET.get('name')
        title = request.GET.get('title')
        article = Commande.objects.create(
            name=name,
            title=title
        )
        article.save()
        article = Commande.objects.all()
        context = {
            "article": article
        }
        return render(request, 'homepage/list.html', context)
    return render(request, 'homepage/list.html')
