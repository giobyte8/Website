from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('learning', views.learning, name='learning'),
    path('blog', views.blog, name='blog')
]