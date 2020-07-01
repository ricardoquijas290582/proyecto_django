from django.urls import path
from .views import GetMovies, GetMovie, CreateMovie, CreateMovieEasy

urlpatterns = [
    #path('movies/', GetMovies)
    path('', GetMovies), #está entrando a la view getmovies
    path('<int:id>/', GetMovie),
    #path('create/', CreateMovie.as_view())
    path('create/', CreateMovieEasy.as_view()),
    path('update/<int:id>/')
]