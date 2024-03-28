from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from social_network_app.models import FriendRequest
from social_network_app.serializers import FriendRequestSerializer
from django.http.response import JsonResponse
from social_network_app.helpers import get_response
from social_network_app.status_code import success


class PendingFriendRequestsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Filter for friend requests where the current user is the receiver and the status is 'sent'
        pending_requests = FriendRequest.objects.filter(
            to_user=request.user,
            status='sent'
        )
        serializer = FriendRequestSerializer(pending_requests, many=True)
        res_obj = get_response(success, serializer.data)
        return JsonResponse(res_obj)