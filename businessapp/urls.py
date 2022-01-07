from . import views
from django.urls import path

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('blog/', views.PostList.as_view(), name='blog'),
    path('post_detail/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('services/', views.services, name='services'),
    path('contacts/', views.contacts, name='contacts'),
    path('thankyou/', views.thankyou, name= 'thankyou'),
    path('contribuition/', views.contribuition, name= 'contribuition'),
    path('Ourgallery/', views.Ourgallery, name = 'Ourgallery'),
    path('trainingPrograme/', views.trainingPrograme, name = 'training'),
    path('Values/', views.Values, name = 'value')
]