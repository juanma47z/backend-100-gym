from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class AuthTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.user_data = {
            'username' : 'test',
            'password1' : 'DA5Jkqr2Vo7q',
            'password2' : 'DA5Jkqr2Vo7q'
            #error en test_register code 200 != 302 problema en la contraseña 
        }

    def test_register(self):
        response = self.client.post(self.register_url, self.user_data)
        print(f"Response content: {response.content}")
        print(f"Response status code: {response.status_code}")
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='test').exists())

    def test_login(self):
        User.objects.create_user(username='test', password='123abc')
        response = self.client.post(self.login_url, {
            'username' : 'test',
            'password' : '123abc'
        })
        self.assertEqual(response.status_code, 302)

    def test_logout(self):
        User.objects.create_user(username='test', password='123abc')
        self.client.login(username='test', password='123abc')
        response = self.client.post(self.logout_url)
        self.assertEqual(response.status_code, 302)

