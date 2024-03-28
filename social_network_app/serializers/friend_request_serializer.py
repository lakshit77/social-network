from rest_framework import serializers
from social_network_app.models import FriendRequest
from django.contrib.auth import get_user_model
User = get_user_model()

class FriendRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendRequest
        fields = ['id', 'from_user', 'to_user', 'status']
        read_only_fields = ('from_user', 'status')  # `from_user` and `status` are handled in the view

class FriendRequestResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendRequest
        fields = ['id', 'status']

    def update(self, instance, validated_data):
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance