from rest_framework.filters import BaseFilterBackend


class VideoFilter(BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        if request.user.is_anonymous:
            return queryset.filter(premium=False)
        else:
            return queryset.all()
