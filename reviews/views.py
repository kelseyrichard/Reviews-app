# Create your views here.

from django.db.models import Avg
from reviewapp.reviews.models import Restaurant, Category, RestaurantType, Review
from django.shortcuts import render_to_response

def homepage(request):
    review = Review.objects.order_by('-pubdate')[:10]
    cuisine_type=Category.objects.order_by('category')
    restaurant_type=RestaurantType.objects.order_by('restaurant_type')
    top_restaurants=Restaurant.objects.annotate(average_rating=Avg('review__rating')).order_by('-average_rating').exclude(average_rating__lte=0)
    return render_to_response('homepage.html', {
        'review' : review,
        'cuisine_type' : cuisine_type,
        'restaurant_type' : restaurant_type,
        'top_restaurants' : top_restaurants,
    })

def restaurant_detail(request, restaurant):
    rest=Restaurant.objects.get(name_slug=restaurant)
    return render_to_response('restaurant_detail.html',{
        'rest':rest,
    })

def rating_detail(request, rating_id):
    review=Review.objects.get(id=rating_id)
    return render_to_response('review_detail.html',{
        'review':review,
    })



def rating(request):
    rating=Rating.objects.order_by('rating')
    return render_to_response('rating_list.html',{
        'rating':rating,
    })

def category(request):
    category = Category.objects.order_by('category')
    return render_to_response('category.html', {
        'category' : category,
    })
