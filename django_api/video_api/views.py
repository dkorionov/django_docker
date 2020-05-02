from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions
from .permissions import IsAuthOrNotPremium
from django_filters.rest_framework import DjangoFilterBackend
from .models import Video
from .filters import VideoFilter
from .serializers import VideoSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from rest_framework.decorators import action
from drf_yasg import openapi
from drf_yasg.app_settings import swagger_settings
from drf_yasg.inspectors import CoreAPICompatInspector, FieldInspector, NotHandled, SwaggerAutoSchema
from drf_yasg.utils import no_body, swagger_auto_schema


class VideoViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Get video
    """
    swagger_schema = SwaggerAutoSchema

    permission_classes = (IsAuthOrNotPremium,)
    pagination_class = PageNumberPagination
    queryset = Video.objects.all().order_by('id')
    serializer_class = VideoSerializer
    filter_backends = (VideoFilter, DjangoFilterBackend)
    filterset_fields = ['premium']

    @action(detail=True, url_path='favorite-add', url_name='add_to_favorite',
            permission_classes=(permissions.IsAuthenticated,))
    def add_favorite(self, request, pk=None):
        """
        Add video to favorite
        """
        video = self.get_object()
        request.user.videos.add(video)
        return Response({'detail': 'added'}, status.HTTP_202_ACCEPTED)

    @action(detail=True, url_path='favorite-remove', url_name='remove_from_favorite',
            permission_classes=(permissions.IsAuthenticated,))
    def remove_favorite(self, request, pk=None):
        """
        Remove from favorite
        """
        video = self.get_object()
        if request.user.videos.remove(video):
            return Response({'detail': 'removed'}, status.HTTP_202_ACCEPTED)
        else:
            return Response({'detail': 'not found'}, status.HTTP_202_ACCEPTED)

    @action(detail=False, url_path='favorites', url_name='favorites',
            permission_classes=(permissions.IsAuthenticated,))
    def favorites(self, request):
        """
        Favorites video
        """
        favorites = request.user.videos.all().order_by('id')
        serialize = self.serializer_class(favorites, many=True)
        return Response(serialize.data, status.HTTP_202_ACCEPTED)
