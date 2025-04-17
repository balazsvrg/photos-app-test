from django.urls import path
from .views import PhotoListCreate, PhotoDelete

urlpatterns = [
    path('photos/', PhotoListCreate.as_view(), name='photo-list-create'),
    path('photos/<int:pk>/', PhotoDelete.as_view(), name='photo-delete'),
]
