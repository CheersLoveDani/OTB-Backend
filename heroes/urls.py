from django.urls import path
from .views import HeroListView, HeroDetailView

urlpatterns = [
    path('', HeroListView.as_view()),
    path('<int:pk>/', HeroDetailView.as_view())
]