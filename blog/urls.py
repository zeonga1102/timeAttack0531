from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.newView, name='new'),
    path('', views.categoryView, name='category'),
    path('<str:category>/', views.articleView, name='article'),
    path('detail/<int:id>', views.detailView, name='detail')
]