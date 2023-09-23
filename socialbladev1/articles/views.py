

from django.http import HttpResponse
from django.views.generic import TemplateView
from django.template import loader


from django.shortcuts import render
from .models import Article  # Import your Article model here



def index(request):
    # You can add any logic here to fetch data or perform other operations if needed
    articles = Article.objects.all()  # Example query to get all articles

    # Render the index.html template with context data
    return render(request, 'articles/index.html', {'articles': articles})


def article_list(request):
    articles = Article.objects.all()
    return render(request, 'articles/article_list.html', {'articles': articles})

def article_detail(request, article_id):
    article = Article.objects.get(pk=article_id)
    return render(request, 'articles/article_detail.html', {'article': article})
