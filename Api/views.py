from django.shortcuts import render, redirect
from django.http import HttpResponse
from Netflix.models.Show import Show, Genre
from Netflix.models.Profile import Profile
from .Serializer import ShowSerializer, ProfileSerializer, RegistrationSerilalizer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import logout



# Create your views here.
@permission_classes([IsAuthenticated,])
class viewShows(generics.ListAPIView):
    queryset = Show.objects.all()
    serializer_class = ShowSerializer

@permission_classes([IsAuthenticated,])
class viewUsers(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

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

# class getUser(generics.ListAPIView):
#     serializer_class = ProfileSerializer
#     def get_queryset(self):
#         user_id = Token.objects.get(key="41afcdf581fe053b59dc38b28ea431fca3081629").user_id
#         users = Profile.objects.all()
#         return users

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
