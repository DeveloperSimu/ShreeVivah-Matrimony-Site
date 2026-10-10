from django.urls import path
from . import views

urlpatterns = [
    path('rahul/', views.rahul, name='rahul'),
    path('brent/', views.brent, name='brent'),
    path('matthew/', views.matthew, name='matthew'),
    path('arjun/', views.arjun, name='arjun'),
    path('karan/', views.karan, name='karan'),
    path('ankita/', views.ankita, name='ankita'),
    path('priya/', views.priya, name='priya'),
    path('ishita/', views.ishita, name='ishita'),
    path('sneha/', views.sneha, name='sneha'),
    path('neha/', views.neha, name='neha'),
    path('details/<slug:slug>/', views.extra_profile, name='extra_profile'),
    # ✅ Search URL
    path('search/', views.profile_search, name='profile_search'),
    path('search/suggestions/', views.profile_name_suggestions, name='profile_name_suggestions'),
]
