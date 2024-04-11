from django.contrib import admin
from ads.models import Ad, Review

@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'description', 'author', 'created_at',)
    list_filter = ('price', 'created_at',)
    search_fields = ('title', 'description',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('text', 'ad', 'author', 'created_at',)
    list_filter = ('ad', 'created_at',)
    search_fields = ('ad', 'author',)