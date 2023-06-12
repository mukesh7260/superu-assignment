from django.shortcuts import render
from superapp.models import Profile 
from superapp.serializers import ProfileSerializer , UserProfileSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework.views import APIView
from rest_framework import status  
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from django.contrib.auth.models import User
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import permissions, status
from rest_framework.validators import ValidationError 
from rest_framework_simplejwt.tokens import RefreshToken


@extend_schema(
request=ProfileSerializer,
)
class Superu(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)

    def post (self, request, format=None):
        serializer = ProfileSerializer(data = request.data) 
        if serializer.is_valid():
            serializer.save() 
            # token = get_tokens_for_user(user)
            return Response({'data':serializer.data,
            'Create':'Profile has created successfully'}, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request,*args,**kwargs):
        id = kwargs.get("pk")
        pro = Profile.objects.get(pk=id)
        serializer = ProfileSerializer(pro, data=request.data) 
        if serializer.is_valid():
            serializer.save() 
            return Response({'data':serializer.data, 'Update':'Profile data updated successfully '}) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def patch(self, request, *args,**kwargs):
        id = kwargs.get("pk") 
        pro = Profile.objects.get(id=id)
        serializer = ProfileSerializer(pro, data=request.data,partial=True) 
        if serializer.is_valid():
            serializer.save() 
            return Response({'data':serializer.data, 'Update':'Profile data partially updated successfully '}) 
        return Response(serializer.errors)
    

class Profilelogin(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class  = UserProfileSerializer
    def post(self,request,*args):
        serializer = UserProfileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.get(username=serializer.data.get('username'))
        if user :
            password = user.check_password(serializer.data.get('password'))
            if not password:
                raise ValidationError({'password':'invalid password'})
            refresh = RefreshToken.for_user(user)
            data  = {
                        'refresh': str(refresh),
                        'access': str(refresh.access_token),
                    }
            return Response(data,status=status.HTTP_201_CREATED)
            
            

#username : mukesh 
#password : admin 
