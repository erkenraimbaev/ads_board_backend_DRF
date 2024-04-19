from rest_framework import status
from rest_framework.test import APITestCase

from ads.models import Ad, Review
from users.models import User
from django.urls import reverse


class AdTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='test@test.com')
        self.user.set_password('1234')
        self.user.save()

        self.admin = User.objects.create(email='moderator@moderator.com', is_staff=True)
        self.admin.set_password('1234')
        self.admin.save()

        self.client.force_authenticate(user=self.user)

        self.ad = Ad.objects.create(
            author=self.user,
            title='Машина',
            price=1000000,
            description='Супер',
        )
        self.ad.save()

        self.review = Review.objects.create(
            text="Test",
            ad=self.ad,
        )
        self.review.save()

    def test_create_ad(self):
        """Тест для создания объявления"""
        url = reverse('ads:ads-create')
        data = {
            'title': 'Дом',
            'price': 1000000,
            'description': 'Супер',
        }
        self.client.force_authenticate(user=self.user)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Ad.objects.count(), 2)

    def test_create_ad_not_right(self):
        """Тест для создания объявления с неверными данными"""
        url = reverse('ads:ads-create')
        data_error = {
            'title': 'Дом',
            'price': 'Test',
            'description': 'Супер',
        }
        response = self.client.post(url, data_error, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_review(self):
        """Тест для создания отзыва"""
        url = reverse('ads:reviews-create')
        data = {
            'text': 'Дом супер',
            'ad': 4,
        }
        self.client.force_authenticate(user=self.user)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Review.objects.count(), 2)

    def test_list_ads(self):
        """Получение списка объявлений"""
        url = reverse('ads:ads-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.client.force_authenticate(user=self.admin)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)
        self.assertEqual(Ad.objects.count(), 1)

    def test_list_my_ads(self):
        """Список моих объявлений"""
        url = reverse('ads:my-ads-list')
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)

    def test_retrieve_ad(self):
        """Информации об объявлении"""
        url = reverse('ads:ad-detail', kwargs={'pk': self.ad.id})
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Машина')

    def test_update_ad(self):
        """Обновлениe объявления"""
        url = reverse('ads:ad-update', kwargs={'pk': self.ad.pk})
        data = {'title': 'Дача',
                'price': 800000}
        self.client.force_authenticate(user=self.user)
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Дача')

    def test_delete_ad(self):
        """Удаление объявления"""
        url = reverse('ads:ad-delete', kwargs={'pk': self.ad.id})
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Ad.objects.count(), 0)
