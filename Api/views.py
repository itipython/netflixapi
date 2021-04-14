# Imported Packages and Classes
from Netflix.models.Profile import Profile, WatchLater, Watched
from Netflix.models.Show import Show, Genre
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view, permission_classes
from .Serializer import ShowSerializer, ProfileSerializer, RegistrationSerilalizer, WatchLaterSerializer, WatchedSerializer
from django.http import HttpResponse
from rest_framework.views import APIView



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

# Logged in User
@api_view(('GET',))    
def currentUser(request):
    user = ProfileSerializer(request.user)
    return Response(user.data)


# Edit User Profile
@permission_classes([IsAuthenticated])
class UpdateProfile(generics.UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


# Get Movies of category
@permission_classes([IsAuthenticated])
class getCategory_Movies(generics.ListAPIView):
    serializer_class = ShowSerializer
    def get_queryset(self):
        category = self.kwargs.get('name')
        movies = Show.objects.filter(genres__name=category)
        return (movies)


#  Get Show and Add it to History list
@api_view(('GET',)) 
@permission_classes([IsAuthenticated])
def getShow(request, name):
    show = Show.objects.get(name=name)
    serializer = ShowSerializer(show)
    user = request.user

    history, created = Watched.objects.update_or_create(Show_id=show, User_id=user)

    return Response(serializer.data)



# View User History
@api_view(('GET',))    
@permission_classes([IsAuthenticated])
def userHistory(request):
    user = ProfileSerializer(request.user)
    user_queryset = Watched.objects.filter(User_id=user.data['id'])
    show_ids = []

    for q in user_queryset:
        show_ids.append(q.Show_id_id)
    
    shows_list = Show.objects.filter(id__in=show_ids)
    serializer = ShowSerializer(shows_list, many=True)
    return Response(serializer.data)



# Delete Show from History
@api_view(('DELETE',))   
@permission_classes([IsAuthenticated])
def removeHistory(request, id):
    user = request.user
    show = Watched.objects.filter(User_id=user,Show_id=id).delete()
    return Response(data={
        "Message":"Show is removed from your History"
    })



# Add Show to Watch Later List
@api_view(['POST',])
@permission_classes([IsAuthenticated])
def addWatchLater(request):
    myshow ={"Show_id":request.data.get("Show_id"),"User_id":request.user.pk}
    show = WatchLaterSerializer(data=myshow, partial=True)
    if show.is_valid():
        show.save()
        return Response(data={
            "Message":" show %s is Added to My List" %show.data["Show_id"]
        })
    else:
        return Response(data={
            'Sucess':'false',
            'Error': show.errors
            },status=status.HTTP_400_BAD_REQUEST
        )


# View Watch Later List
@api_view(('GET',))    
@permission_classes([IsAuthenticated])
def viewWatchLater(request):
    user = ProfileSerializer(request.user)
    user_queryset = WatchLater.objects.filter(User_id=user.data['id'])
    show_ids = []

    for q in user_queryset:
        show_ids.append(q.Show_id_id)
    
    shows_list = Show.objects.filter(id__in=show_ids)
    serializer = ShowSerializer(shows_list, many=True)
    return Response(serializer.data)



# Delete Show from Watch Later
@api_view(('DELETE',))   
@permission_classes([IsAuthenticated])
def removeLater(request, id):
    user = request.user
    show = WatchLater.objects.filter(User_id=user,Show_id=id).delete()
    return Response(data={
        "Message":"Show is removed from your show later list"
    })