from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from users.apps import UsersConfig
from users.views import UserDetailView, MyTokenObtainPairView, SetPasswordView, ProfileDetailOrProfileUpdateView, \
    UserListOrCreateView

app_name = UsersConfig.name

urlpatterns = [path('users/', UserListOrCreateView.as_view(), name='users-list-or-create'),
               path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
               path('users/me/', ProfileDetailOrProfileUpdateView.as_view(), name='my-profile'),
               path('users/set_password/', SetPasswordView.as_view(), name='set-password'),
               path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
               path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
               ]
