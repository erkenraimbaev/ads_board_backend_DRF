from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from users.models import User
from users.serializers import UserSerializer, MyTokenObtainPairSerializer, UserNewPasSerializer


class UserListView(generics.ListCreateAPIView):
    """
    Пользователи сервиса
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    """
    Посмотреть профиль
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProfileDetailView(generics.RetrieveUpdateAPIView):
    """
    Посмотреть свой профиль
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        obj = get_object_or_404(User, pk=self.request.user.pk)
        return obj


class MyTokenObtainPairView(TokenObtainPairView):
    """
    Получить токен
    """
    serializer_class = MyTokenObtainPairSerializer


class UserCreateView(generics.ListCreateAPIView):
    """
    Создать пользователя
    """
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(user.password)
        user.save()


class UserUpdateView(generics.RetrieveUpdateAPIView):
    """
    Обновить пользователя
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_update(self, serializer):
        user = serializer.save()
        user.save()


class SetPasswordView(APIView):
    """
    Изменить пароль
    """
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserNewPasSerializer

    def post(self, request):
        user = self.request.user
        data = request.data
        new_password = data.get('new_password')
        current_password = data.get('current_password')
        if user.check_password(current_password):
            user.set_password(new_password)
            user.save()
            message = 'Ваш пароль успешно обновлен!'
        else:
            message = 'Неверно введен ваш старый пароль!'
        return Response({"message": message})
