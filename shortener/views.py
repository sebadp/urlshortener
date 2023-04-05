from rest_framework import generics, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import ShortenedURL
from .serializers import ShortenedURLSerializer


class ShortenedURLViewSet(viewsets.ModelViewSet):
    queryset = ShortenedURL.objects.all()
    serializer_class = ShortenedURLSerializer

    @action(detail=True, methods=['get'])
    def redirect(self, request, pk=None):
        shortened_url = self.get_object()
        return Response({'long_url': shortened_url.long_url}, status=status.HTTP_301_MOVED_PERMANENTLY)


class Top100ShortenedURLs(generics.ListAPIView):
    queryset = ShortenedURL.objects.all().order_by('-updated_at')[:100]
    serializer_class = ShortenedURLSerializer
