from django.urls import path

from ads.apps import AdsConfig
from ads.views import ReviewsCreateAPIView, MyAdsListView, AdsReviewsDetailView, AdsListView, AdsCreateView, \
    ReviewsDetailAPIView, AdsDetailView, AdsDeleteView, AdsUpdateView, ReviewsUpdateAPIView, ReviewsDeleteAPIView


app_name = AdsConfig.name

urlpatterns = [
    path('ads/', AdsListView.as_view(), name='ads-list'),
    path('ads/create/', AdsCreateView.as_view(), name='ads-create'),
    path('ads/me/', MyAdsListView.as_view(), name='my-ads-list'),
    path('ads/<int:pk>/', AdsDetailView.as_view(), name='ad-detail'),
    path('ads/update/<int:pk>/', AdsUpdateView.as_view(), name='ad-update'),
    path('ads/delete/<int:pk>/', AdsDeleteView.as_view(), name='ad-delete'),
    path('ads/<int:pk>/comments/', AdsReviewsDetailView.as_view(), name='ad-detail-reviews'),
    path('ads/comments/create/', ReviewsCreateAPIView.as_view(), name='reviews-create'),
    path('ads/<int:pk_ad>/comments/<int:pk>/', ReviewsDetailAPIView.as_view(), name='reviews-detail'),
    path('ads/<int:pk_ad>/comments/update/<int:pk>/', ReviewsUpdateAPIView.as_view(), name='reviews-update'),
    path('ads/<int:pk_ad>/comments/delete/<int:pk>/', ReviewsDeleteAPIView.as_view(), name='reviews-delete'),

]
