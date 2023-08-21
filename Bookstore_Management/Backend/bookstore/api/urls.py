from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'books', views.BookListView, basename="book")
# router.register(r'users', views.UserViewSet,basename="user")# multiple user use

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('books/', views.BookListView.as_view()), # get and post request handle korbe
]