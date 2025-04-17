from django.db import models

from django.db import models

class Photo(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='photos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    tags = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title

