# from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from django.contrib.auth import get_user_model
from social_network_app.serializers import UserSerializer
from social_network_app.filters import UserFilter
from social_network_app.helpers import BaseCustomModelViewSet

User = get_user_model()

class UserSearchViewSet(BaseCustomModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = UserFilter
    http_method_names = ['get']
    permission_classes = [permissions.IsAuthenticated]