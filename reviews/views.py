# Create your views here.

from django.http import HttpResponse
from reviewapp.reviews.models import Rating, Category, Business, Review
from django.shortcuts import render_to_response

def homepage(request):
    review = Review.objects.order_by('name_of_business')
    return render_to_response('homepage.html', {
        'review' : review,
    })

def rating(request):
    rating=Rating.objects.order_by('rating')
    return render_to_response('rating_list.html',{
        'rating':rating,
    })
