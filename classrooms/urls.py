from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ResultViewSet
from . import views
router = DefaultRouter()
router.register(r'classrooms', ResultViewSet)

urlpatterns = [
    path('classroom/', views.classroom_list_view, name='classroom_list'),
    path('classroom/add/', views.classroom_create_view, name='classroom_create'),
    path('classroom/<int:pk>/', views.classroom_detail_view, name='classroom_detail'),
    path('classroom/<int:pk>/edit/', views.classroom_edit_view, name='classroom_edit'),

    #DRF apis endpoint
    path('api/', include(router.urls)),
]