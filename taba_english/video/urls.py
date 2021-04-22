from rest_framework import routers
from video.views import VideoViewSet
router = routers.SimpleRouter()
router.register(r'videos', VideoViewSet)

