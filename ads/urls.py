from django.urls import path

from ads.apps import AdsConfig
from ads.views import ReviewsCreateAPIView, MyAdsListView, AdsReviewsDetailView, AdsListOrCreateView, \
    AdsDetailOrUpdateOrDeleteView, \
    ReviewsDetailOrUpdateOrDeleteAPIView

app_name = AdsConfig.name

urlpatterns = [
    path('ads/', AdsListOrCreateView.as_view(), name='ads-list-or-create'),
    path('ads/me/', MyAdsListView.as_view(), name='my-ads-list'),
    path('ads/<int:pk>/', AdsDetailOrUpdateOrDeleteView.as_view(), name='ad-detail-update-delete'),
    path('ads/<int:pk>/comments/', AdsReviewsDetailView.as_view(), name='ad-detail-reviews'),
    path('ads/<int:pk>/comments/create/', ReviewsCreateAPIView.as_view(), name='reviews-create'),
    path('ads/<int:pk_ad>/comments/<int:pk>/', ReviewsDetailOrUpdateOrDeleteAPIView.as_view(),
         name='reviews-detail-update-delete'),

]
