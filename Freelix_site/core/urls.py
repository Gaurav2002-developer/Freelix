from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('login', views.login, name = 'login'),
    path('signup', views.signup, name = 'signup'),
    path('home', views.home, name = 'home'),
    path('profile', views.profile, name = 'profile'),
    path('movies', views.movies, name='movies'),
    # path('movies/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('tv', views.tv, name='tv'),
    path('movies/<str:pk>/', views.movie_detail, name='movie_detail'),
    path('search', views.search, name = 'search'),                   
]