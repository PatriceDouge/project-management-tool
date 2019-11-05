from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from rest_framework_jwt.settings import api_settings

#inheriting from ModelSerializer to generate validators for the serializer based on the model
class UserSerializer(serializers.ModelSerializer):
    #emailField is required for all Users and is unique
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    #username is required for all Users, max of 32 characters and are unique
    username = serializers.CharField(
            max_length=32,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    #password req to have min lenght of 6 chars
    password = serializers.CharField(min_length=6,write_only=True)

    #jwt token
    token = serializers.SerializerMethodField()

    #method to get user token
    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    #creating a new User using djangos anthentication system
    def create(self, validated_data):
        user = User(email=validated_data['email'],
                username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

    #defining that the corresponding model is User and id, username, email and pass are its fields
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password','token')