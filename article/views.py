from datetime import datetime
from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from .models import Article


def home(request):
    s = "Hello World!"
    return HttpResponse(s)


def now(request):
    return render(request, "now.html", {'now': datetime.now()})


def article_detail(request, pk):
    article = Article.objects.get(pk=pk)
    return render(request, 'article_detail.html', {'article': article})


def article_list(request):
    articles = Article.objects.all()
    return render(request, 'article_list.html', {'articles': articles})


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', ]


def article_form(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            new_article = form.save()
            return HttpResponseRedirect('/article/' + str(new_article.pk))

    form = ArticleForm()
    return render(request, 'article_form.html', {'form': form})
