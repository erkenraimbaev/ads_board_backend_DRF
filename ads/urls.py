from django.urls import path, include

from ads.apps import AdsConfig
from ads.views import AdsListView, AdsDetailView, AdsCreateView, AdsUpdateView, AdsDeleteView, ReviewsCreateAPIView, \
    ReviewsDetailAPIView, ReviewsUpdateAPIView, ReviewsDeleteAPIView, MyAdsListView, \
    AdsReviewsDetailView

app_name = AdsConfig.name

urlpatterns = [
    path('ads/', AdsListView.as_view(), name='ads-list'),
    path('ads/me/', MyAdsListView.as_view(), name='my-ads-list'),
    path('ads/<int:pk>/', AdsDetailView.as_view(), name='ad-detail'),
    path('ads/<int:pk>/comments/', AdsReviewsDetailView.as_view(), name='ad-detail-reviews'),
    # path('ads/', AdsCreateView.as_view(), name='ads-create'),
    # path('ads/<int:pk>/', AdsUpdateView.as_view(), name='ads-update'),
    # path('ads/<int:pk>/', AdsDeleteView.as_view(), name='ads-delete'),
    # path('ads/<int:pk>/comments/', ReviewsCreateAPIView.as_view(), name='reviews-create'),
    # path('reviews/<int:pk>/comments/', ReviewsDeleteAPIView.as_view(), name='reviews-delete'),
    # path('ads/<int:pk>/comments/', ReviewsDetailAPIView.as_view(), name='reviews-detail'),
    # path('ads/<int:pk>/comments/', ReviewsUpdateAPIView.as_view(), name='reviews-update'),
]
