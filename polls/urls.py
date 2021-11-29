from django.urls import path
from . import views
app_name = 'polls'
urlpatterns = [
    # # /polls/
    # path('', views.index, name='index'),
    # # /polls/1/  使用尖括号“捕获”部分 URL 并将其作为关键字参数发送给视图函数
    # path('<int:question_id>/', views.detail, name='detail'),
    # # /polls/1/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # # /polls/1/results/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    # path('',views.index,name='index')
    path('', views.IndexView.as_view(), name='index'),
    # path('<int:question_id>/', views.detail, name='detail'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:question_id>/results/', views.results, name='results'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
