from django.urls import path
from .views import GetMovies, GetMovie, CreateMovie, CreateMovieEasy, UpdateMovie, DeleteMovie

app_name='movies'
urlpatterns = [
    #path('movies/', GetMovies)
    path('', GetMovies, name='list'), #está entrando a la view getmovies
    path('<int:id>/', GetMovie, name='detail'),
    #path('create/', CreateMovie.as_view())
    path('create/', CreateMovieEasy.as_view(), name='create'),
    path('update/<int:id>/', UpdateMovie.as_view(), name='update'),
    path('delete/<int:id>/', DeleteMovie, name='delete')
]