from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from ads.permissions import IsAuthor
from users.models import User
from users.serializers import UserSerializer, MyTokenObtainPairSerializer, UserNewPasSerializer


class UserListView(generics.ListAPIView):
    """
    Пользователи сервиса
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UserCreateView(generics.CreateAPIView):
    """
    Создать пользователя
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(user.password)
        user.save()


class UserDetailView(generics.RetrieveAPIView):
    """
    Посмотреть профиль пользователя
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class ProfileDetailOrProfileUpdateView(generics.RetrieveUpdateAPIView):
    """
    Посмотреть свой профиль
    или
    Обновить свой профиль
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAuthor]

    def get_object(self):
        obj = get_object_or_404(User, pk=self.request.user.pk)
        return obj

    def perform_update(self, serializer):
        user = serializer.save()
        user.set_password(user.password)
        user.save()


class MyTokenObtainPairView(TokenObtainPairView):
    """
    Получить токен
    """
    serializer_class = MyTokenObtainPairSerializer


class SetPasswordView(APIView):
    """
    Изменить пароль
    """

    queryset = User.objects.all()
    serializer_class = UserNewPasSerializer
    permission_classes = [IsAuthenticated, IsAuthor]

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
