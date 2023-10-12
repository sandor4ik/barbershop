from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.productsPage, name='products'),
    path('book/', views.bookPage, name='book'),
    path('products/<int:pk>/', views.productDetail, name='product_detail'),

    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutCustomer, name='logout'),
    path('customer-account/<str:pk>/', views.updatePage, name='customer-account'),
    path('update-password/<str:pk>/', views.updatePassword, name='change-password'),
    
    path('book/barbershop/<str:barbershop_name>/', views.barbershop, name='barbershop'),
    path('book/services/<str:selected_barber>/', views.services, name='services'),
    path('book/choose_day/<int:service_id>/', views.chooseDay, name='choose_day'),
    path('book/choose_time/', views.chooseTime, name='choose_time'),
    path('book/appointment_confirmation/', views.appointmentConfirmation, name='appointment_confirmation'),
    path('book/save_appointment/', views.saveAppointment, name='save_appointment'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)