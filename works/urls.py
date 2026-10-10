from django.urls import path
from . import views

urlpatterns = [
    path('work/', views.work, name='work'),
    path('services/', views.services, name='services'),
    path('plans/', views.plans, name='plans'),
    path('firstlook/', views.firstlook, name='firstlook'),
    path('mehendi/', views.mehendi, name='mehendi'),
    path('haldi/', views.haldi, name='haldi'),
    path('fire/', views.fire, name='fire'),
    path('together/', views.together, name='together'),
    path('hand/', views.hand, name='hand'),
]
