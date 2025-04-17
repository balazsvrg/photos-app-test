from rest_framework import generics
from .models import Photo
from .serializers import PhotoSerializer

class PhotoListCreate(generics.ListCreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

class PhotoDelete(generics.DestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
