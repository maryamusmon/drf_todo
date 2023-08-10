
import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from users.services.cache_function import getKey, setKey


@pytest.mark.django_db
class TestActivationUserGenericAPIView:
    activate_code = ''
    client = APIClient()
    payload = dict(

        email="diordev@icloud.com",
        username="diordev",
        password="b2002234",
        re_password="b2002234",
    )

    urls = {
        'register': reverse('register'),
        'activate': reverse('activated_account'),

    }

    @pytest.fixture
    def test_user_register(self):
        response = self.client.post(self.urls.get('register'), self.payload)

        data = response.data
        assert response.status_code == status.HTTP_201_CREATED
        assert "password" not in data
        assert data["email"] == self.payload["email"]

    def test_user_activation(self, test_user_register):
        data = {
            'email': self.payload.get('email'),
            'activation_code': getKey(self.payload.get('email'))
        }
        response = self.client.post(self.urls.get('activate'), data)
        assert response.status_code == status.HTTP_200_OK

    def test_user_activation_invalid_data(self):
        data = {'email': 'invalid-email'}
        response = self.client.post(self.urls.get('activate'), data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
