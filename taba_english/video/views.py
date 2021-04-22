from rest_framework import viewsets
from video.models import Video
from video.serializers import VideoSerializer


# Create your views here.
class VideoViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Video.objects.all()
	serializer_class = VideoSerializer

