from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from django.conf.urls import url


urlpatterns = [
    path('', include('rest_framework.urls')),
    path(('category/<str:name>'), views.getCategory_Movies.as_view()),
    path(('movie/<str:name>'), views.getShow),    
    
    path(('shows/'), views.viewShows.as_view()),
    path(('users/'), views.viewUsers.as_view()),
    path(('register/'), views.Registration),

    # It must be login not login/
    path('login', obtain_auth_token),
    
    # /logout/, /user/ --> Current logged in user , /password/change/ 
    url('rest-auth/', include('rest_auth.urls')),

    path('update/<int:pk>/',views.UpdateProfile.as_view()),
    path('addlater/',views.addWatchLater),
    path('watchlater/',views.viewWatchLater),
    path('watchlater/<int:id>',views.removeLater),
    path('history/',views.userHistory),
    path('history/<int:id>',views.removeHistory),
    path('user/',views.currentUser)
]
