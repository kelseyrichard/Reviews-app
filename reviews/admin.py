from django.contrib import admin
from reviews.models import Restaurant, Category, RestaurantType, Review


admin.site.register(RestaurantType)
admin.site.register(Category)
admin.site.register(Restaurant)
admin.site.register(Review)


