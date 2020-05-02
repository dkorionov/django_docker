from rest_framework import status
from django.urls import reverse
from rest_framework.test import (APITestCase,
                                 APIClient)
from video_api.models import Video
from auth_api.models import User
from video_api.serializers import VideoSerializer

client = APIClient()


class VideoTests(APITestCase):
    """
    Test video functional
    """
    fixtures = ['../django_api/fixture/fixture.json']


    @classmethod
    def setUpTestData(cls):
        User.objects.create(username='tester', password='test123')

    # def setUpTestData(self):

    def tearDown(self):
        client.logout()

    def test_auth_video(self):
        """
        Test get all video for auth users
        :return:
        """
        user = User.objects.get(username='tester')
        client.force_authenticate(user)
        serialize, response = self.video_helper()
        self.assertEqual(serialize.data, response.data['results'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_non_auth_video(self):
        """
        Test get only no-premium video for non-auth users
        :return:
        """
        serialize, response = self.video_helper(premium=False)
        self.assertEqual(serialize.data, response.data['results'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_non_auth_access_premium(self):
        """
        Test get access to premium video from non-auth users
        :return:
        """
        video = Video.objects.filter(premium=True).first()
        url = reverse('video-detail', kwargs={'pk': video.pk})
        response = client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_add_to_favorite(self):
        """
        Test add video to favorite
        :return:
        """
        user, url = self.favorite_helper('video-add_to_favorite')
        client.force_authenticate(user)
        response = client.get(url)
        self.assertEqual(user.videos.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)

    def test_remove_from_favorite(self):
        """
        Test remove video from favorite
        :return:
        """
        self.test_add_to_favorite()
        user, url = self.favorite_helper('video-remove_from_favorite')
        self.test_add_to_favorite()
        response = client.get(url)
        self.assertEqual(user.videos.count(), 0)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)

    def test_non_auth_favorite(self):
        """
        Test access non-ath users add video to favorite
        :return:
        """
        user, url = self.favorite_helper('video-add_to_favorite')
        response = client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def video_helper(self, **kwargs):
        """
        Find the number of objects on the page and doing slice in query
        :return: serializer, response
        """
        url = reverse('video-list')
        response = client.get(url)
        count = len(response.data['results'])
        if kwargs:
            video = Video.objects.filter(premium=kwargs['premium']).order_by('id')
        else:
            video = Video.objects.filter().order_by('id')
        serializer = VideoSerializer(video[:count], many=True)
        return serializer, response

    def favorite_helper(self, url_name):
        """
        Find user and video url
        :param url_name:
        :return: user, url
        """
        user = User.objects.get(username='tester')
        video = Video.objects.first()
        url = reverse(url_name, kwargs={'pk': video.pk})
        return user, url
