from django.urls import reverse 
from django.contrib.auth import get_user_model

from rest_framework.test import APITestCase

User = get_user_model()

class UsersAPIViewsTests(APITestCase):

    def test_signup_api_view_is_working(self):
        url = reverse('users:signup_api_view')
        body = {'email': 'umamabauma@gmail.com','password': 'www1234'}
        response = self.client.post(url,body, format='json')
        self.assertEquals(response.status_code,201)
        user = User.objects.filter(email=body['email']).first()
        self.assertIsNotNone(user)
        self.assertTrue(user.check_password(body['password']))

    def test_signup_api_view_no_double_emails(self):
        user = User.objects.create_user(email='umamabauma@gmail.com',password= 'www1234')
        url = reverse('users:signup_api_view')
        body = {'email': 'umamabauma@gmail.com','password': 'www1234'}
        response = self.client.post(url,body,format='json')
        self.assertEquals(response.status_code, 400)
