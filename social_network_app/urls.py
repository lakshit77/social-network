from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SignupView, LoginView, UserSearchViewSet, FriendRequestViewSet, FriendRequestResponseView, ListFriendsView, PendingFriendRequestsView

router = DefaultRouter()
router.register(r'search_friends', UserSearchViewSet, basename='user-search')
# router.register(r'friend-requests', FriendRequestViewSet)

urlpatterns = [
    path('auth/signup/', SignupView.as_view(), name='signup'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('friend-requests/create/', FriendRequestViewSet.as_view({'post': 'create'})),
    path('friend-requests/delete/<int:pk>', FriendRequestViewSet.as_view({'delete': 'destroy'})),
    path('friend-requests/respond/<int:pk>/', FriendRequestResponseView.as_view(), name='friend-request-respond'),
    path('friend-requests/pending/', PendingFriendRequestsView.as_view(), name='pending-friend-requests'),
    path('list_my_friends/', ListFriendsView.as_view(), name='list-friends'),
    path('', include(router.urls))
]