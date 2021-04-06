from django.shortcuts import render
from django.http import HttpResponse
from Netflix.models.Show import Show
from Netflix.models.Profile import Profile
from .Serializer import ShowSerializer, UserSerializer, RegistrationSerilalizer
from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated



# Create your views here.
# @permission_classes([IsAuthenticated,])
class viewShows(generics.ListAPIView):
    queryset = Show.objects.all()
    serializer_class = ShowSerializer

# @permission_classes([IsAuthenticated,])
class viewUsers(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = UserSerializer

@api_view(['POST',])
def Registration(request):
    serializer = RegistrationSerilalizer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={
            'Success':'True',
            'Message':'User %s Added Sucessfully' %serializer.data['first_name']
            },status=status.HTTP_201_CREATED
        )
    return Response(data={
        'Sucess':'false',
        'Error': serializer.errors
        },status=status.HTTP_400_BAD_REQUEST
    )





