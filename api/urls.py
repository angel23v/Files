from django.urls import path, include
from rest_framework import routers
from api import views
from .views import FileUploadView, FolderViewSet

router = routers.DefaultRouter()
router.register(r'file', views.FileViewSet)
router.register(r'folder', views.FolderViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('upload/', FileUploadView.as_view(), name='file-upload'),

]
