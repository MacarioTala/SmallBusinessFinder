"""
Definition of urls for SmallBusinessFinder.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views

app_name = 'app'

urlpatterns = [
    path('', views.IndexView.as_view(),name='index'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('submitRestaurant/', views.submitRestaurant, name='submitRestaurant'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
    path('api/restaurants/',views.restaurant_list),
    path('api/restaurants/<int:pk>/',views.restaurant_detail,name='restaurant_detail_api'),
	path('restaurants/<int:pk>/',views.ViewRestaurantDetails.as_view(),name='restaurant_detail'),
	path('enterRestaurant/',views.enterRestaurant,name='enterRestaurant')
]
