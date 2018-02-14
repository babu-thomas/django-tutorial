from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.ListView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail')
]