from django.urls import path
from django.conf.urls.static import static
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('services/<str:pk>/', views.edit_service, name='edit_service'),
    path('services/delete/<str:pk>/', views.delete_service, name='delete_service'),
    path('services', views.services, name='services'),
    path('transactions', views.transactions, name='transactions'),
    path('transactionsfilter', views.transactions_filter, name='transactions_filter'),
    path('barbers', views.barbers, name='barbers'),
    path('barbers/delete/<str:pk>/', views.delete_barber, name='delete_barber'),
    path('reception', views.reception, name='reception'),
    path('summary', views.summary, name='summary'),
    path('sidebar', views.sidebar, name='sidebar'),
]
