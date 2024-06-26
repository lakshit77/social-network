from rest_framework import status, permissions
from rest_framework.decorators import action
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from social_network_app.models import FriendRequest
from social_network_app.serializers import FriendRequestSerializer, FriendRequestResponseSerializer, FriendRequestResponsePostSerializer
from social_network_app.helpers import BaseCustomModelViewSet, get_response
from social_network_app.status_code import success
from django.http.response import JsonResponse
from social_network_app.utils import is_rate_limited
from social_network_app.status_code import rate_limit_for_user, invalid_user_action, generic_error_3

class FriendRequestViewSet(BaseCustomModelViewSet):
    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(from_user=self.request.user)  # Automatically set the sender to the current user
    
    @action(methods=['post'], detail=False)
    def create(self, request, *args, **kwargs):
        if is_rate_limited(request.user.id):
            res_obj = get_response(rate_limit_for_user)
            return JsonResponse(res_obj, status=429)  # 429 Too Many Requests
        
        return super(FriendRequestViewSet, self).create(request, *args, **kwargs)

class FriendRequestResponseView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        request_body=FriendRequestResponsePostSerializer,
        responses={
            201: openapi.Response('Signup successful', FriendRequestResponseSerializer)
        }
    )
    def post(self, request, pk):
        friend_request = FriendRequest.objects.get(pk=pk)
        response = request.data.get('status')

        if friend_request.to_user != request.user:
            res_obj = get_response(invalid_user_action)
            return JsonResponse(res_obj, status=status.HTTP_403_FORBIDDEN)

        if response not in ['accepted', 'rejected']:
            res_obj = get_response(generic_error_3)
            return JsonResponse(res_obj, status=status.HTTP_400_BAD_REQUEST)

        serializer = FriendRequestResponseSerializer(instance=friend_request, data={'status': response}, partial=True)
        if serializer.is_valid():
            serializer.save()
            res_obj = get_response(success, serializer.data)
            return JsonResponse(res_obj)
        else:
            res_obj = get_response(success, serializer.errors)
            return JsonResponse(res_obj, status=status.HTTP_400_BAD_REQUEST)