from rest_framework import serializers

from ads.models import Ad, Review


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class AdDetailSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(source='review_ad', read_only=True, many=True)

    class Meta:
        model = Ad
        fields = '__all__'
