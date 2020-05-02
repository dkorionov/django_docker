from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import SerializerMethodField
from .models import Video
from django.urls import reverse_lazy
from django.db import models


class VideoSerializer(ModelSerializer):
    add_to_favorite_url = SerializerMethodField('create_add_favorite_url')
    remove_from_favorite_url = SerializerMethodField('create_rem_favorite_url')

    class Meta:
        model = Video
        fields = ('pk', 'video', 'title', 'description',
                  'load_at', 'premium', 'add_to_favorite_url', 'remove_from_favorite_url')
        ordering = ['id']



    def create_add_favorite_url(self, video):
        return reverse_lazy('video-add_to_favorite', kwargs={'pk': video.pk})

    def create_rem_favorite_url(self, video):
        return reverse_lazy('video-remove_from_favorite', kwargs={'pk': video.pk})
