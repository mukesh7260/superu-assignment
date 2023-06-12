from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Profile

class MyModelAPIViewTest(APITestCase):
    def setUp(self):
        self.url = reverse('create')
        self.instance = Profile.objects.create(name='Test Object')

    def test_get_object(self):
        detail_url = reverse('Profile', args=[self.instance.pk])
        response = self.client.get(detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_object(self):
        data = {'name': 'New Object','email':'skfjs@gmail.com','bio':'skfs','profile_picture':''}
        print(data)
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Profile.objects.count(), 1)
        self.assertEqual(Profile.objects.first().name, data['name']) 

    def test_update_object(self):
        detail_url = reverse('create/<int:pk>/', args=[self.instance.pk])
        data = {'name': 'Updated Object'}
        response = self.client.put(detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_object(self):
        detail_url = reverse('mymodel-detail', args=[self.instance.pk])
        response = self.client.delete(detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
