from django.http import response
from rest_framework import authentication
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from . serializers import RegisterSerializer, ProfileSerialiezer
from django.contrib.auth.models import User
from . models import Profile
from rest_framework import status
from rest_framework import viewsets
from rest_framework_simplejwt.tokens import RefreshToken
# for registration
from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer
#for login 
from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
#for authentication and pemission
from rest_framework. authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerialiezer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]



################# using APIView #########################

# class ProfileView(APIView):
    # def get(self, request, pk=None, format=None):
    #     id = pk
    #     if id is not None:
    #         profile = Profile.objects.get(id=pk)
    #         serializer = ProfileSerialiezer(profile)
    #         return Response(serializer.data) 

    #     profile = Profile.objects.all()
    #     serializer = ProfileSerialiezer(profile, many=True)
    #     return Response(serializer.data)

    # def post(self, request, format=None):
    #     # import pdb;pdb.set_trace()
    #     # file_obj = request.FILES
    #     serializer = ProfileSerialiezer(data=request.data)

    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'msg': 'data created'}, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
    # def put(self, request, pk, format=None):
    #     id = pk
    #     profile = Profile.objects.get(id=pk)
    #     serializer = ProfileSerialiezer(profile, request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'msg': 'complete data updated'})
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    # def patch(self, request, pk, format=None):
    #     id = pk
    #     profile = Profile.objects.get(id=pk)
    #     serializer = ProfileSerialiezer(profile, request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'msg': 'partialy data updated'})
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # def delete(self, request, pk, format=None):
    #     id = pk 
    #     profile = Profile.objects.get(id=pk)
    #     profile.delete()
    #     return Response({'msg': 'data deleted'})




################    using ViewSet    ##############################

#class ProfileViewSet(viewsets.ViewSet):
    # def list(self, request):
    #     profile = Profile.objects.all()
    #     serializer = ProfileSerialiezer(profile, many=True)
    #     return Response(serializer.data) 


    # def retrieve(self, request, pk=None):
    #     id = pk
    #     if id is not None:
    #         profile = Profile.objects.get(id=pk)
    #         serializer = ProfileSerialiezer(profile)
    #         return Response(serializer.data)


    # def create(self, request):
    #     data = {
    #         'user': request.user,
    #         'image': request.data.get('image'),
    #         'caption': request.data.get('caption')
    #     }
    #     serializer = ProfileSerialiezer(data=data)
    #     # import pdb; pdb.set_trace()
    #     if serializer.is_valid():
    #          serializer.save()
    #          return Response({'msg': 'profile created'}, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    # def update(self, request, pk):
    #     id = pk
    #     profile = Profile.objects.get(pk=id)
    #     serializer = ProfileSerialiezer(profile, data=request.data)
    #     if serializer.is_valid():
    #          serializer.save()
    #          return Response({'msg': 'complete data updated'})
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # def partial_update(self, request, pk):
    #     id = pk
    #     profile = Profile.objects.get(pk=id)
    #     serializer = ProfileSerialiezer(profile, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'msg': 'complete data updated'})
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # def destroy(self, request, pk):
    #     id = pk
    #     profile = Profile.objects.get(pk=id)
    #     profile.delete()
    #     Response({'msg': 'profile deleted sucsessfully'})



############### register, login, using JWT(JSON WEB TOKEN) ##########

# create your views 

# class RegisterAPIView(APIView):
#     serializer_class = RegisterSerializer

#     def post(self, request, format=None):
#         serializer = self.serializer_class(data=request.data)

#         if serializer.is_valid():
#             user = serializer.save()

#             refresh = RefreshToken.for_user(user)

#             response_data =  {
#              'refresh': str(refresh),
#              'access': str(refresh.access_token),
#             }
#             return Response(response_data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class LogoutView(APIView):

#     def post(self, request):
#         try:
#             refresh_token = request.data["refresh_token"]
#             token = RefreshToken(refresh_token)
#             token.blacklist()

#             return Response(status=status.HTTP_205_RESET_CONTENT)
#         except Exception as e:
#             return Response(status=status.HTTP_400_BAD_REQUEST)

