from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from ads.models import Ad, Review
from ads.paginators import AdsPaginator
from ads.permissions import IsAuthor, IsAdmin
from ads.serializers import AdSerializer, ReviewSerializer, AdDetailSerializer
from ads.filters import MyAdsFilter


class AdsListView(generics.ListAPIView):
    """
    Вывести список всех объявленийе
    """
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    pagination_class = AdsPaginator
    filter_backends = (DjangoFilterBackend,)
    filterset_class = MyAdsFilter


class AdsCreateView(generics.CreateAPIView):
    """
    Создать объявление
    """
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated, ~IsAdmin]

    def perform_create(self, serializer):
        new_ad = serializer.save()
        new_ad.author = self.request.user
        new_ad.save()


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


class AdsUpdateOrDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
    Обновить объявление
    или
    Удалить объявление
    """
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated, IsAuthor | IsAdmin]

    def perform_update(self, serializer):
        update_ad = serializer.save()
        update_ad.author = self.request.user
        update_ad.save()

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


class AdsReviewsDetailView(generics.RetrieveAPIView):
    """
    Подробнее об объявлении с отзывами
    """
    queryset = Ad.objects.all()
    serializer_class = AdDetailSerializer
    permission_classes = [IsAuthenticated | IsAuthor | IsAdmin]


class ReviewsDetailAPIView(generics.RetrieveAPIView):
    """
    Побробнее об отзыве
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated | IsAdmin]

    def get_object(self, **kwargs):
        ad_pk = self.kwargs.get('pk_ad')
        ad_exist = get_object_or_404(Ad, pk=ad_pk)
        review_pk = self.kwargs.get('pk')
        return get_object_or_404(Review, ad=ad_exist, pk=review_pk)


class ReviewsUpdateOrDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Обновить отзыв
    или
    Удалить отзыв
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated, IsAuthor | IsAdmin]

    def get_object(self, **kwargs):
        ad_pk = self.kwargs.get('pk_ad')
        ad_exist = get_object_or_404(Ad, pk=ad_pk)
        review_pk = self.kwargs.get('pk')
        return get_object_or_404(Review, ad=ad_exist, pk=review_pk)

    def perform_update(self, serializer):
        update_review = serializer.save()
        update_review.author = self.request.user
        update_review.save()

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


class ReviewsCreateAPIView(generics.CreateAPIView):
    """
    Создать отзыв
    """
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated | ~IsAdmin]

    def perform_create(self, serializer):
        new_review = serializer.save()
        new_review.author = self.request.user
        new_review.save()
