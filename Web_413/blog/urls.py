from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
     path('article/<int:id>/', views.detail, name='article_detail'), #новый маршрут для просмотра статьи
]
