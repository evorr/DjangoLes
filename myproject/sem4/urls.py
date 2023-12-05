from django.urls import path
from .views import choice_form, author_form, post_form


urlpatterns = [
    path('choice/', choice_form, name='choice_form'),
    path('author/', author_form, name='author_form'),
    path('post/', post_form, name='post_form'),
]