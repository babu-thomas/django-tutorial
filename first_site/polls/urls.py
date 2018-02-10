from django.urls import path
from . import views


app_name = 'polls'
urlpatterns = [
    # /polls/
    path('', views.index, name='index'),
    # /polls/3/
    path('<int:question_id>/', views.detail, name='detail'),
    # /polls/3/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # /polls/3/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
