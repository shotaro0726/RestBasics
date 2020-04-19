from django.urls import path
from . import views

app_name = 'api_basic'

urlpatterns = [
    path('article/', views.article_liat),
    path('detail/<int:pk>/', views.article_detail),
]