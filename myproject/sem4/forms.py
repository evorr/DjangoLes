from django import forms
import datetime
import models


class ChoiceForm(forms.Form):
    game = forms.ChoiceField(choices=[('c', 'coin'), ('b', 'cube'), ('r', 'random')],
                             widget=forms.RadioSelect)
    count = forms.IntegerField(min_value=1, max_value=64, widget=forms.NumberInput(attrs={'class': 'form-control'}))


class AuthorForm(forms.Form):
    name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'user@mail.ru'}))
    biography = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    birthday = forms.DateField(initial=datetime.date.today,
                               widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))


class PostForm(forms.Form):
    title = forms.CharField(label='Название', max_length=50)
    content = forms.CharField(label='Содеожание', widget=forms.Textarea(attrs={'class': 'form-control'}))
    public_date = forms.DateField(initial=datetime.date.today,
                               widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    #author = forms.ChoiceField(choices=[(author.id, str(author)) for author in models.Author.objects.all()])
    author = forms.ModelChoiceField(queryset=models.Author.objects.all())
    category = forms.CharField(max_length=50)
    view_count = forms.IntegerField(min_value=1, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    published = forms.BooleanField(required=False,
                                   widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))


class CommentForm(forms.Form):
    author = forms.ModelChoiceField(queryset=models.Author.objects.all())
    #article = forms.ModelChoiceField(queryset=models.Article.objects.all())
    comment = forms.CharField(label='Содеожание', widget=forms.Textarea(attrs={'class': 'form-control'}))
    created_at = forms.DateField(initial=datetime.date.today,
                               widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    changed_at = forms.DateField(initial=datetime.date.today,
                               widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))


