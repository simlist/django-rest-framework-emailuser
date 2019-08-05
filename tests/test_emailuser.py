import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from emailuser.models import EmailUser

EMAIL = 'me@example.com'
NAME = 'Foo Bar'
PASSWORD = 'MYPASSWORD'

def user_to_dict(user):
    return {
        'id': user.id,
        'email': user.email,
        'name': user.name
    }


class UserTestCase(APITestCase):
    def setUp(self):
        EmailUser.objects.create_user(
            email=EMAIL,
            name=NAME,
            password=PASSWORD
            )
    
    def test_registration(self):
        data = {
            'name': 'Me',
            'email': 'example@gmail.com',
            'password': 'mypassword'
            }
        response = self.client.post(reverse('accounts:register'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        user = EmailUser.objects.get(email=data['email'])
        self.assertEqual(user.email, data['email'])
        self.assertEqual(user.name, data['name'])

    def test_retrieve_user(self):
        user = EmailUser.objects.get(email=EMAIL)
        response = self.client.get('/accounts/users/{}'.format(user.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            'email': EMAIL,
            'name': NAME,
            'id': user.id})
    
    def test_update_user(self):
        user = EmailUser.objects.get(email=EMAIL)
        self.client.force_authenticate(user=user)
        data = {
            'email': EMAIL,
            'name': NAME + ' new',
            'id': user.id
        }
        response = self.client.put(
            reverse('accounts:update', args=[user.id,]),
            {'email': data['email'], 'name': data['name'], 'password': 'slyeshiva'}, 
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated_user = EmailUser.objects.get(email=EMAIL)

        self.assertEqual(user_to_dict(updated_user), data)
    
    def test_patch_user(self):
        user = EmailUser.objects.get(email=EMAIL)
        self.client.force_authenticate(user=user)
        response = self.client.patch(
            reverse('accounts:update', args=[user.id,]),
            {'name': user.name + ' patch'}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        patched_user = EmailUser.objects.get(id=user.id)
        self.assertEqual(patched_user.name, NAME + ' patch')

    def test_patch_password(self):
        user = EmailUser.objects.get(email=EMAIL)
        self.client.force_authenticate(user=user)
        response = self.client.patch(
            reverse('accounts:update', args=[user.id,]),
            {'password': 'mypatchedpassword'}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        token_response = self.client.post(
            reverse('token_obtain_pair'),
            {'email': user.email, 'password': 'mypatchedpassword'}
        )
        self.assertEqual(token_response.status_code, status.HTTP_200_OK)


    def test_create_superuser(self):
        data = {
            'email': 'admin@example.com',
            'name': 'Super User',
            'password': 'MySuperPassword'
        }
        EmailUser.objects.create_superuser(**data)
        superuser = EmailUser.objects.get(email=data['email'])
        self.assertEqual(superuser.name, data['name'])
        self.assertTrue(superuser.is_superuser)
    
    def test_email_lowercased(self):
        EmailUser.objects.create_user(
            name=NAME + '2',
            email='UPPER@example.com',
            password=PASSWORD
        )
        user = EmailUser.objects.get(email='upper@example.com')
        self.assertEqual(user.name, NAME + '2')
            