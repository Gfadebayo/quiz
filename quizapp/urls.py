
from django.urls import path
from . import views

app_name="quizapp"
urlpatterns = [
    path('', views.home, name='home'),
    #read the comments in utils to understand why section is used instead of category
    path('<str:section_id>/question/', views.question, name='question'),
    path('result/', views.result, name='result'),
    path('review/', views.review, name='review'),
    #path('<str:section>/', views.category, name='category'),
]
