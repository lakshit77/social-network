from rest_framework import serializers
from social_network_app.models import FriendRequest

class FriendRequestResponsePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendRequest
        fields = ['status']

    def validate_status(self, value):
        if value not in ['accepted', 'rejected']:
            raise serializers.ValidationError("Invalid response. Choose 'accepted' or 'rejected'.")
        return value