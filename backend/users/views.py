from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.serializers import UserSerializer
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from rest_framework import permissions, status
from rest_framework.decorators import api_view

@api_view(['GET'])
def current_user(request):
    """
    Determine the current user by their token, and return their data
    """
    
    serializer = UserSerializer(request.user)
    return Response(serializer.data)

#defining an APIView for creating a user
class UserCreate(APIView):
    """ 
    Creates the user. 
    """
        
    permission_classes = (permissions.AllowAny,)    

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
