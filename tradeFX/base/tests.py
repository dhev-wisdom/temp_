from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class AuthenticationTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_user_registration(self):
        response = self.client.post(reverse('register'), {'username': 'user1', 'password': 'pass1'})
        self.assertEqual(response.status_code, 201)

    def test_user_login(self):
        response = self.client.post(reverse('login'), {'username': 'testuser1', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue('token' in response.data)

    def test_protected_view_access(self):
        response = self.client.get(reverse('traders_list'))
        self.assertEqual(response.status_code, 401)

        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('traders_list'))
        self.assertEqual(response.status_code, 200)

