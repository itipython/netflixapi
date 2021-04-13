# Imported Packages and Classes
from Netflix.models.Profile import Profile, WatchLater
from Netflix.models.Show import Show, Genre
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view, permission_classes
from .Serializer import ShowSerializer, ProfileSerializer, RegistrationSerilalizer, WatchLaterSerializer
from django.http import HttpResponse


# Create your views here.

# List All Shows
@permission_classes([IsAuthenticated,])
class viewShows(generics.ListAPIView):
    queryset = Show.objects.all()
    serializer_class = ShowSerializer
    filter_backends = [DjangoFilterBackend]


# List All Users
@permission_classes([IsAuthenticated,])
class viewUsers(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

# User Registration Api View
@api_view(['POST',])
def Registration(request):
    serializer = RegistrationSerilalizer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={
            'Success':'True',
            'Message':'User %s Added Sucessfully' %serializer.data['username']
            },status=status.HTTP_201_CREATED
        )
    return Response(data={
        'Sucess':'false',
        'Error': serializer.errors
        },status=status.HTTP_400_BAD_REQUEST
    )


@permission_classes([IsAuthenticated])
class UpdateProfile(generics.UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class getCategory_Movies(generics.ListAPIView):
    serializer_class = ShowSerializer
    def get_queryset(self):
        category = self.kwargs.get('name')
        movies = Show.objects.filter(genres__name=category)
        return (movies)

class getMovie(generics.ListAPIView):
    serializer_class = ShowSerializer
    def get_queryset(self):
        movieName = self.kwargs.get('name')
        movie = Show.objects.filter(name=movieName)
        return movie

@api_view(['POST',])
@permission_classes([IsAuthenticated])
def addWatchLater(request):
    show = WatchLaterSerializer(data=request.data)
    if show.is_valid():
        show.save()
        return Response(data={
            "Message":" show %s is Added to My List" %show.data["show"]
        })
    else:
        return Response(data={
            'Sucess':'false',
            'Error': show.errors
            },status=status.HTTP_400_BAD_REQUEST
        )

 

@api_view(('GET',))    
@permission_classes([IsAuthenticated])
def viewWatchLater(request):
    user = ProfileSerializer(request.user)
    user_queryset = WatchLater.objects.filter(user=user.data['id'])
    show_ids = []

    for q in user_queryset:
        show_ids.append(q.show_id)
    
    shows_list = Show.objects.filter(id__in=show_ids)
    serializer = ShowSerializer(shows_list, many=True)
    return Response(serializer.data)




@api_view(('GET',))    
def currentUser(request):
    user = ProfileSerializer(request.user)
    return Response(user.data)
    