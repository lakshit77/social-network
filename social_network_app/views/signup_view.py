from rest_framework import views
from rest_framework.authtoken.models import Token
from social_network_app.serializers import SignupSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.http.response import JsonResponse

from social_network_app.status_code import success, generic_error_2, generic_error_1
from social_network_app.helpers import get_response, CustomExceptionHandler

# User registration view
class SignupView(views.APIView):
    @swagger_auto_schema(
        request_body=SignupSerializer,
        responses={
            201: openapi.Response('Signup successful', SignupSerializer),
            400: 'Bad Request'
        }
    )
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        try:
            if not serializer.is_valid():
                return JsonResponse(get_response(generic_error_2, serializer.errors))

            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            response_obj = get_response(success, {"token": token.key})
                
        except CustomExceptionHandler as e:
            response_obj = get_response(eval(str(e)))
        except Exception as e:
            response_obj = get_response(generic_error_1)
        
        return JsonResponse(response_obj)

# User login view
