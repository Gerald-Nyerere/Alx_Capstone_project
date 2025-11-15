from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet
from . import views
from .views import dashboard_view


router = DefaultRouter()
router.register(r'students', StudentViewSet)

urlpatterns = [
    path('student/', views.student_list_view, name='student_list'),
    path('student/dashboard/', dashboard_view, name='dashboard'),
    path('student/add/', views.student_create_view, name='student_create'),
    path('student/<int:pk>/', views.student_detail_view, name='student_detail'),

    path('api/', include(router.urls)),
]