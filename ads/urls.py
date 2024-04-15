from django.urls import path

from ads.apps import AdsConfig
from ads.views import ReviewsCreateAPIView, MyAdsListView, AdsReviewsDetailView, ReviewsUpdateOrDeleteAPIView, \
    AdsListView, AdsCreateView, ReviewsDetailAPIView, AdsDetailView, AdsUpdateOrDeleteView

app_name = AdsConfig.name

urlpatterns = [
    path('ads/', AdsListView.as_view(), name='ads-list'),
    path('ads/create/', AdsCreateView.as_view(), name='ads-create'),
    path('ads/me/', MyAdsListView.as_view(), name='my-ads-list'),
    path('ads/<int:pk>/', AdsDetailView.as_view(), name='ad-detail'),
    path('ads/<int:pk>/', AdsUpdateOrDeleteView.as_view(), name='ad-update-delete'),
    path('ads/<int:pk>/comments/', AdsReviewsDetailView.as_view(), name='ad-detail-reviews'),
    path('ads/comments/create/', ReviewsCreateAPIView.as_view(), name='reviews-create'),
    path('ads/<int:pk_ad>/comments/<int:pk>/', ReviewsDetailAPIView.as_view(), name='reviews-detail'),
    path('ads/<int:pk_ad>/comments/<int:pk>/', ReviewsUpdateOrDeleteAPIView.as_view(), name='reviews-update-delete'),
]
