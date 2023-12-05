from django.urls import path
from .views import main, about, coin, cube, rnd100, get_articles


urlpatterns = [
    path('', main, name='main'),
    path('about/', about, name='about'),
    path('coin/', coin, name='coin'),
    path('cube/', cube, name='cube'),
    path('rnd100/', rnd100, name='rnd100'),
    path('get/<int:author_id>/', get_articles),
]
