from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User

#inheriting from ModelSerializer to generate validators for the serializer based on the model
class UserSerializer(serializers.ModelSerializer):
    #emailField is required for all Users and is unique
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    #username is required for all Users and are unique
    username = serializers.CharField(
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    #password req to have min lenght of 6 chars
    password = serializers.CharField(min_length=6,write_only=True)

    #creating a new User using djangos anthentication system
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
             validated_data['password'])
        return user

    #defining that the corresponding model is User and id, username, email and pass are its fields
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')