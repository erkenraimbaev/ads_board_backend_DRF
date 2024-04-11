from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from ads.models import Ad, Review
from ads.paginators import AdsPaginator
from ads.permissions import IsAuthor, IsAdmin
from ads.serializers import AdSerializer, ReviewSerializer, AdDetailSerializer


class AdsListView(generics.ListCreateAPIView):
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


class AdsDetailView(generics.RetrieveUpdateDestroyAPIView):
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


class AdsCreateView(generics.ListCreateAPIView):
    """
    Создать объявление
    """
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated, ~IsAdmin]

    def perform_create(self, serializer):
        new_ad = serializer.save()
        new_ad.author = self.request.user
        new_ad.save()


class AdsUpdateView(generics.RetrieveUpdateDestroyAPIView):
    """
    Обновить объявление
    """
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated & IsAuthor | IsAdmin]

    def perform_update(self, serializer):
        update_ad = serializer.save()
        update_ad.author = self.request.user
        update_ad.save()


class AdsDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
    Удалить объявление
    """
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated & IsAuthor | IsAdmin]

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


class ReviewsDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
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


class ReviewsCreateAPIView(generics.CreateAPIView):
    """
    Создать отзыв
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated | ~IsAdmin]

    def perform_create(self, serializer):
        new_review = serializer.save()
        new_review.author = self.request.user
        new_review.save()


class ReviewsUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Обновить отзыв
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated & IsAuthor | IsAdmin]

    def get_object(self, **kwargs):
        ad_pk = self.kwargs.get('pk_ad')
        ad_exist = get_object_or_404(Ad, pk=ad_pk)
        review_pk = self.kwargs.get('pk')
        return get_object_or_404(Review, ad=ad_exist, pk=review_pk)

    def perform_update(self, serializer):
        update_review = serializer.save()
        update_review.save()


class ReviewsDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Удалить отзыв
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated & IsAuthor | ~IsAdmin]

    def get_object(self, **kwargs):
        ad_pk = self.kwargs.get('pk_ad')
        ad_exist = get_object_or_404(Ad, pk=ad_pk)
        review_pk = self.kwargs.get('pk')
        return get_object_or_404(Review, ad=ad_exist, pk=review_pk)

    def perform_destroy(self, instance):
        super().perform_destroy(instance)
