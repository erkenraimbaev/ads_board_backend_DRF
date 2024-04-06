from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from ads.models import Ad, Review
from ads.paginators import AdsPaginator
from ads.permissions import IsAuthor, IsAdmin
from ads.serializers import AdSerializer, ReviewSerializer, AdDetailSerializer


class AdsListView(generics.ListAPIView):
    """
    Вывести список всех объявлений
    """
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    pagination_class = AdsPaginator


class MyAdsListView(generics.ListAPIView):
    """
    Вывести список объявлений авторизованного пользователя
    """
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated & IsAuthor | IsAdmin]
    pagination_class = AdsPaginator

    def get_queryset(self):
        return Ad.objects.filter(author=self.request.user)


class AdsDetailView(generics.RetrieveAPIView):
    """
    Подробнее об объявлении
    """
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated | IsAuthor | IsAdmin]


class AdsReviewsDetailView(generics.RetrieveAPIView):
    """
    Подробнее об объявлении с отзывами
    """
    queryset = Ad.objects.all()
    serializer_class = AdDetailSerializer
    permission_classes = [IsAuthenticated | IsAuthor | IsAdmin]


class AdsCreateView(generics.CreateAPIView):
    """
    Создать объявление
    """
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated, ~IsAdmin]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.author = self.request.user
        new_lesson.save()


class AdsUpdateView(generics.UpdateAPIView):
    """
    Обновить объявление
    """
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated & IsAuthor | IsAdmin]

    def perform_update(self, serializer):
        update_lesson = serializer.save()
        update_lesson.owner = self.request.user
        update_lesson.save()


class AdsDeleteView(generics.DestroyAPIView):
    """
    Удалить объявление
    """
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated & IsAuthor | IsAdmin]

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


class ReviewsDetailAPIView(generics.RetrieveAPIView):
    """
    Побробнее об отзыве
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated | IsAdmin]


class ReviewsCreateAPIView(generics.CreateAPIView):
    """
    Создать отзыв
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated | ~IsAdmin]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.author = self.request.user
        new_lesson.save()


class ReviewsUpdateAPIView(generics.UpdateAPIView):
    """
    Обновить отзыв
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated & IsAuthor | IsAdmin]

    def perform_update(self, serializer):
        update_lesson = serializer.save()
        update_lesson.owner = self.request.user
        update_lesson.save()


class ReviewsDeleteAPIView(generics.DestroyAPIView):
    """
    Удалить отзыв
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated & IsAuthor | ~IsAdmin]

    def perform_destroy(self, instance):
        super().perform_destroy(instance)
