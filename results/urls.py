from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ResultViewSet
from . import views
router = DefaultRouter()
router.register(r'results', ResultViewSet)

urlpatterns = [
    path('result/', views.result_list_view, name='result_list'),
    path('result/add/', views.result_create_view, name='result_create'),
    path('result/<int:pk>/', views.result_detail_view, name='result_detail'),

    #DRF api endpoint
    path('api/', include(router.urls)),
]