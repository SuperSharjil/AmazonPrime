from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:id>/', views.VideoDetail, name="Detail"),
    path('trending/', views.Trending, name="Trending"),
    path('movies/', views.Movies, name="Movies"),
    path('series/', views.Series, name="Series"),
    path('series/<int:id>/', views.SeriesDetails, name="SeriesDetails"),
    path('search/', views.GetTitle, name="GetTitle"),
    path('rate/<int:id>/', views.Rate, name="Rate"),
    path('cast/<int:id>/', views.Cast, name="Cast"),
    path('movies/franchise/', views.MoviesFranchise, name="MoviesFranchise"),
    path('movies/franchise/<int:id>/', views.MoviesFranchiseDetails, name="MoviesFranchiseDetails"),
]
