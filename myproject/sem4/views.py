from django.shortcuts import render, get_object_or_404
from random import randint
from .forms import ChoiceForm, AuthorForm, PostForm, CommentForm
from .models import Author, Article, Comment


def coin(request):
    result = randint(0, 1)
    result = 'Решка' if result else 'Орел'
    return result



def cube(request):
    result = randint(1, 6)
    return result


def rnd100(request):
    result = randint(1, 100)
    return result


def choice_form(request):
    if request.method == 'POST':
        form = ChoiceForm(request.POST)
        if form.is_valid():
            game = form.cleaned_data['game']
            count = form.cleaned_data['count']
            if game == 'c':
                result = coin(request)
                return render(request, 'sem4/base_coin.html', {'result': result})
            elif game == 'b':
                result = cube(request)
                return render(request, 'sem4/base_coin.html', {'result': result})
            elif game == 'r':
                result = rnd100(request)
                return render(request, 'sem4/base_coin.html', {'result': result})
    else:
        form = ChoiceForm()
    return render(request, 'sem4/choice.html', {'form': form})


def author_form(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            biography = form.cleaned_data['biography']
            birthday = form.cleaned_data['birthday']
            author = Author(name=name, last_name=last_name, email=email, biography=biography, birthday=birthday)
            author.save()
    else:
        form = AuthorForm()
    return render(request, 'sem4/author.html', {'form': form})


def post_form(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            public_date = form.cleaned_data['public_date']
            author = form.cleaned_data['author']
            category = form.cleaned_data['category']
            view_count = form.cleaned_data['view_count']
            published = form.cleaned_data['published']
            post = Article(title=title, content=content, public_date=public_date, author=author, category=category,
                           view_count=view_count, published=published)
            post.save()
    else:
        form = PostForm()
    return render(request, 'sem4/post.html', {'form': form})


def comment_form(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            author = form.cleaned_data['author']
            comment = form.cleaned_data['comment']
            created_at = form.cleaned_data['created_at']
            changed_at = form.cleaned_data['changed_at']
            comment = Comment(author=author, comment=comment, created_at=created_at, changed_at=changed_at)
            comment.save()
    else:
        form = CommentForm()
    return render(request, 'sem4/comment`.html', {'form': form})