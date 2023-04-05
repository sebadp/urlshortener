# urls.py
from django.urls import path
from rest_framework import routers
from .views import ShortenedURLViewSet, Top100ShortenedURLs

router = routers.SimpleRouter()
router.register(r'', ShortenedURLViewSet)

urlpatterns = [
    path('top100/', Top100ShortenedURLs.as_view(), name='top_100_shortened_urls'),
]

urlpatterns += router.urls
