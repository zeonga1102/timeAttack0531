from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.showNew, name='new'),
    path('', views.showCategory, name='category'),
    path('<category>/', views.showArticleList, name='article'),
]