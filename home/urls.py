from django.urls import path
from .views import HomeView


# Not given url for now, Kept for later.
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    # path('', home, name="home"),
]