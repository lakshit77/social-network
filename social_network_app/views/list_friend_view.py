from django.db.models import Q
from rest_framework import generics
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from social_network_app.models import FriendRequest
from social_network_app.serializers import UserSerializer
from social_network_app.helpers import get_response
from social_network_app.status_code import success
from rest_framework.response import Response

User = get_user_model()

class ListFriendsView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def custom_response(self, serializer):
        res_obj = get_response(success, serializer.data)
        return Response(res_obj)

    def get_queryset(self):
        user = self.request.user
        # Query to find where the current user is involved in an accepted friend request
        friend_requests = FriendRequest.objects.filter(
            (Q(from_user=user) | Q(to_user=user)) & Q(status='accepted')
        )

        # Compiling a list of user IDs from those friend requests
        friend_ids = set()
        for fr in friend_requests:
            if fr.from_user == user:
                friend_ids.add(fr.to_user.id)
            else:
                friend_ids.add(fr.from_user.id)
        
        # Querying for users based on those IDs
        friends = User.objects.filter(id__in=friend_ids).distinct()
        return friends

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return self.custom_response(serializer)