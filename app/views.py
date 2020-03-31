"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, JsonResponse,HttpRequest, Http404, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
import app.models as m
from app.serializers import RestaurantSerializer
from datetime import datetime
from django.template import loader
from django.urls import reverse
from django.views import generic
from app.forms import SubmitRestaurantForm
from app.models import Restaurant
from django.contrib import messages

class IndexView(generic.ListView):
	template_name = 'app/index.html'
	context_object_name = 'restaurant_list'

	def get_queryset(self):
		return m.Restaurant.objects.filter(isLive=True)

class ViewRestaurantDetails(generic.DetailView):
	model = m.Restaurant
	template_name='app/restaurantDetail.html'

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'FeedMe Seattle',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def enterRestaurant(request):
	assert isinstance(request,HttpRequest)
	return render(
		request,
		'FoodFinderWeb/createRestaurant.html',
		{
			'title':'Enter My Restaurant',
			'year':datetime.now().year,
		}
	)

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'The Feed Me Seattle Project',
            'message':'Keeping our local small businesses alive',
            'year':datetime.now().year,
        }
    )

def submitRestaurant(request):
	if request.method == 'POST':
		restaurant = m.Restaurant()
		restaurant.name = request.POST['restaurant-name']
		restaurant.address = request.POST['restaurant-address']
		restaurant.phoneNumber = request.POST['restaurant-phone']
		restaurant.city = 'Seattle'
		restaurant.isLive = True

		if Restaurant.objects.filter(name=restaurant.name):
			messages.add_message(request, messages.INFO,"Looks like this place is popular. It's already on here.",fail_silently=True)
			return render(request,'app/submitRestaurant.html',{'title':'Submit Restaurant','message':"Looks like this place is popular. It's already on here."})
		else:
			restaurant.save()
			messages.add_message(request, messages.INFO,"Thanks for submitting this restaurant",fail_silently=True)
			return render(request,'app/submitRestaurant.html',{'title':'Submit Restaurant','message':"Thanks for submitting this restaurant"})
		
	else:
		messages 
	return render(
        request,
        'app/submitRestaurant.html',
        {	
		    'title':'Submit Restaurant',
            'year':datetime.now().year,
			'message': ''
        }
    )

#API Section
@csrf_exempt
def restaurant_list(request):
	
	if request.method == 'GET':
		restaurants = m.Restaurant.objects.filter(isLive=True)
		serializer = RestaurantSerializer(restaurants,many=True)
		return JsonResponse(serializer.data, safe=False)
		
	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = RestaurantSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def restaurant_detail(request,pk):
	try:
		restaurant = m.Restaurant.objects.get(pk=pk)
	except m.Restaurant.DoesNotExist:
		return HttpResponse(status=404)
	
	if request.method == "GET":
		serializer = RestaurantSerializer(restaurant)
		return JsonResponse(serializer.data)
	
	if request.method == "PUT":
		data = JSONParser().parse(request)
		serializer = RestaurantSerializer(restaurant,data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data)
		return JsonResponse(serializer.errors,status=400)
		
	elif request.method == "DELETE":
		restaurant.delete()
		return HttpResponse(status=204)
	
