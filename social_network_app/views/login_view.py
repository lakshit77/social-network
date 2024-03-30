from rest_framework import status, views
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.http.response import JsonResponse

from social_network_app.status_code import success, generic_error_2, generic_error_1, invalid_credential
from social_network_app.helpers import get_response, CustomExceptionHandler

# Define manual request schema for the login endpoint
login_request = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'email': openapi.Schema(type=openapi.TYPE_STRING, description='User email'),
        'password': openapi.Schema(type=openapi.TYPE_STRING, description='User password'),
    },
    required=['email', 'password']
)


class LoginView(views.APIView):
    @swagger_auto_schema(
        request_body=login_request,  # Use the manually defined request schema
        responses={
            200: openapi.Response('Login successful', 
                                  schema=openapi.Schema(
                                      type=openapi.TYPE_OBJECT,
                                      properties={
                                          'token': openapi.Schema(type=openapi.TYPE_STRING, description='Authentication Token')
                                      })),
            400: 'Bad Request',
        },
        operation_description="Login with email and password",
    )
    def post(self, request):
        try:
            email = request.data.get('email').lower()
            password = request.data.get('password')
            user = authenticate(email=email, password=password)
            if user:
                token, created = Token.objects.get_or_create(user=user)
                response_obj = get_response(success, {"token": token.key})
            else:
                return JsonResponse(get_response(invalid_credential))
                
        except CustomExceptionHandler as e:
            response_obj = get_response(eval(str(e)))
        except Exception as e:
            response_obj = get_response(generic_error_1)
        
        return JsonResponse(response_obj)
