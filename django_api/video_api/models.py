from django.db import models
from django.urls import reverse


class Video(models.Model):
    video = models.FilePathField(verbose_name='video_url', path='media/video/')
    title = models.CharField(max_length=255)
    description = models.TextField()
    load_at = models.DateTimeField(auto_now=True)
    premium = models.BooleanField(default=False)
    REQUIRED_FIELDS = ['video', 'title', 'premium']

    def __str__(self):
        return str(self.video)
