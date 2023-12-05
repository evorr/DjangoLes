from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from datetime import datetime
from random import randint
from django.views import View
from django.views.generic import TemplateView
from .models import Author, Article, Comment


def main(request):
    context = {'name': "Elena"}
    return render(request, 'sem3/main.html', context)


def about(request):
    context = {'datetime': datetime.now(), 'client_ip': get_client_ip(request)}
    return render(request, 'sem3/about.html', context)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def coin(request):
    result = randint(0, 1)
    result = 'Решка' if result else 'Орел'
    context = {'result': result}
    return render(request, 'sem3/base_coin.html', context)


def cube(request):
    result = randint(1, 6)
    context = {'result': result}
    return render(request, 'sem3/base_coin.html', context)


def rnd100(request):
    result = randint(1, 100)
    context = {'result': result}
    return render(request, 'sem3/base_coin.html', context)


def get_articles(request, author_id):
    articles = Article.objects.filter(author__pk=author_id)
    context = {'articles': articles}
    return render(request, 'sem3/templ.html', context)