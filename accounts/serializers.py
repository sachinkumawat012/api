from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile


class ProfileSerialiezer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = [ 'image', 'caption', 'user']

        
from rest_framework import serializers
from django.contrib.auth.models import User

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user




# class RegisterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = [ 'username', 'email', 'password', ]
#         extra_kwargs = {
#             'password': {'write_only': True}
#         }


#     def create(self, validated_data):
#         username = validated_data.get('username')
#         email = validated_data.get('email')
#         password = validated_data.get('password')

#         user = User(username=username, email=email)
#         user.set_password('password')
#         user.save()
#         return user
