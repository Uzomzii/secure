from django.urls import path
from .views import (HomePageView,
                    AboutPageView,
                    ServicePageView,
                    ContactPageView,
                    BlogPageView,
                    BlogDetailView,
                    )

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('services/', ServicePageView.as_view(), name='services'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('blog/', BlogPageView.as_view(), name='blog'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),

]
