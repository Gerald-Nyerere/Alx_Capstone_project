from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SubjectViewSet
from . import views

router = DefaultRouter()
router.register(r'subjects', SubjectViewSet)

urlpatterns = [
    #Front end
    path("subject/", views.subject_list_view, name="subject_list"),
    path("subject/create/", views.subject_create_view, name="subject_create"),
    path("subject/<int:pk>/", views.subject_detail_view, name="subject_detail"),

    #backend apis DRF
    path('api/', include(router.urls)),
]