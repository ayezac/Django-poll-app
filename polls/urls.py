from django.urls import path
from . import views 

app_name = 'polls'
urlpatterns = [
    path('', views.index, name ='index'),
    path('<int:question_id>/', views.detail, name = 'detail'),
    path('<int:question_id>/results/', views.results, name = 'results'),
    path('<int:question_id>/vote/', views.vote, name ='vote'),
    path('signup/', views.SignUp.as_view(), name = 'signup'),
    path('add_question/', views.add_question, name = 'add_question' ),
    path('save_poll/', views.save_poll, name='save_poll'),
    path('questions/', views.QuestionList.as_view()),
]
    