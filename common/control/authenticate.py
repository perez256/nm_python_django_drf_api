from rest_framework import exceptions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from common.control.jwt_authent import JWTAuthentication
from common.control.serializers import UserSerializer

# -- register
from core.models import User


class RegisterAPIView(APIView):
    def post(self, incoming):
        data = incoming.data
        if data['password'] != data['password_confirm']:
            raise exceptions.AuthenticationFailed('Passwords do not match')

        data['is_beneficiary'] = 'api/beneficiary' in incoming.path

        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


# login
class LoginAPIView(APIView):
    def post(self, incoming):
        email = incoming.data['email']
        password = incoming.data['password']

        user = User.objects.filter(email__contains=email).first()
        if user is None:
            raise exceptions.AuthenticationFailed('User not found!')
        if not user.check_password(password):
            raise exceptions.AuthenticationFailed('Incorrect Password!')

        # scope
        scope = 'beneficiary' if 'api/beneficiary' in incoming.path else 'admin'
        if user.is_beneficiary and scope == 'admin':
            raise exceptions.AuthenticationFailed('You are unauthorized')

        token = JWTAuthentication.generate_jwt(user.id, scope)
        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {'message': 'success'}
        return response


# get authenticated user
class UserAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, incoming):
        user = incoming.user
        data = UserSerializer(incoming.user).data
        return Response(data)


# logout user
class LogoutAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, _):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {'message': 'success'}
        return response


# update the logged in user details
class ProfileAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, incoming, pk=None):
        user = incoming.user
        serializer = UserSerializer(user, data=incoming.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


# Reset your  password
class ProfilePasswordAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, incoming, pk=None):
        user = incoming.user
        data = incoming.data
        if data['password'] != data['password_confirm']:
            raise exceptions.AuthenticationFailed('Passwords do not match')
        user.set_password(data['password'])
        user.save()
        return Response(UserSerializer(user).data)
