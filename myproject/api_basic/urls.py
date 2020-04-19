from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'api_basic'
router = DefaultRouter()
router.register('article', views.ArticleViewSet, basename='article')

urlpatterns = [
    # path('article/', views.article_liat),
    path('article/',views.ArticleAPIView.as_view()),
    path('article/<int:pk>/',views.ArticleAPIView.as_view()),
    path('article/generics/<int:id>/', views.GenericAPIView.as_view()),
    path('detail/<int:id>/', views.ArticleDetail.as_view()),
    path('viewset/', include(router.urls)),
]
