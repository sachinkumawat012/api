from django.db.models.fields import files
from django.http import response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers import PostSerializer

# Create your views here.

class PostApi(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            post = Post.objects.get(id=pk)
            serializer = PostSerializer(post)
            return Response(serializer.data) 

        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # import pdb;pdb.set_trace()
        # file_obj = request.FILES
        serializer = PostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'data created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
    def put(self, request, pk, format=None):
        id = pk
        post = Post.objects.get(id=pk)
        serializer = PostSerializer(post, request.data)
        if serializer.is_valid():
            serializer.save()
            return response({'msg': 'complete data updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def patch(self, request, pk, format=None):
        id = pk
        post = Post.objects.get(id=pk)
        serializer = PostSerializer(post, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return response({'msg': 'partialy data updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        id = pk 
        post = Post.objects.get(id=pk)
        post.delete()
        return response({'msg': 'data deleted'})
        