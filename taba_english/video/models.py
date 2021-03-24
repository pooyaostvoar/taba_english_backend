from django.db import models

# Create your models here.
from django.db import models
from django_minio_backend import MinioBackend, iso_date_prefix
class Video(models.Model):
    file = models.FileField(verbose_name="Object Upload",
                            storage=MinioBackend(bucket_name='django-backend-dev-private'),
                            upload_to=iso_date_prefix)
    name = models.TextField()