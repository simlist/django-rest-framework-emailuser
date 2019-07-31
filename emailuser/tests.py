import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from .models import EmailUser

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
        response = self.client.post('/accounts/register/', data)
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

""" pytestmark = pytest.mark.django_db 
@pytest.fixture(scope='module')
def api_client():
    return APIClient()

@pytest.fixture(scope='function')
def user_init():
    data = {
        'name': 'sim list',
        'email': 'me@example.com',
        'password': 'mypassword'
    }
    client = APIClient()
    request = client.post('/accounts/register/', data, format='json')
    return data

def test_create_user(api_client, user_init):
    EMAIL = user_init['email']
    NAME = user_init['name']
    PASSWORD = user_init['password']

    user = models.EmailUser.objects.get(email=EMAIL)
    assert user.name == NAME
    assert user.email == EMAIL
    assert user.is_staff == False
    assert user.is_superuser == False
        
def test_update_user(user_init, api_client):
    user = models.EmailUser.objects.get(email=user_init['email'])
    assert user.name == user_init['name']
    put = api_client.put(
        '/accounts/user/{}'.format(str(user.id)),
        {'name': user.name + ' updated'},
        format='json'
        )
    updated_user = models.EmailUser.objects.get(id=user.id)
    assert updated_user.name == (user.name + ' updated')

def test_retrieve_user(user_init, api_client):
    user = models.EmailUser.objects.get(email=user_init['email'])
    id = user.id
    response = api_client.get(
        '/accounts/users/{}'.format(str(id)),
        content_type='application/json',
        format='json'
        ).json()
    assert response['email'] == user.email
    assert response['name'] == user.name
 """