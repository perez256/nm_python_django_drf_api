import datetime

import jwt
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions

from core.models import User
from nm_motors import settings


class JWTAuthentication(BaseAuthentication):
    def authenticate(self, incoming):
        is_beneficiary = 'api/beneficiary' in incoming.path

        token = incoming.COOKIES.get('jwt')
        if not token:
            return None
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('Unauthenticated')

        user = User.objects.get(pk=payload['user_id'])

        if (is_beneficiary and payload['scope'] != 'beneficiary') or (not is_beneficiary and payload['scope'] != 'admin'):
            raise exceptions.AuthenticationFailed('Invalid access scope')

        if user is None:
            raise exceptions.AuthenticationFailed('User not found!')
        return user, None

    @staticmethod
    def generate_jwt(id, scope):
        payload = {
            'user_id': id,
            'scope': scope,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
            'iat': datetime.datetime.utcnow()
        }

        return jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
