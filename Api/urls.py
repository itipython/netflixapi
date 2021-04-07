from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('', include('rest_framework.urls')),
    path(('shows/'), views.viewShows.as_view()),
    path(('users/'), views.viewUsers.as_view()),
    path(('register/'), views.Registration),
    # It must be login not login/
    path('login', obtain_auth_token),
    path('logout', views.logout)
]
