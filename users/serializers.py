from django.contrib.auth import authenticate
from rest_framework import serializers
from users.models import UserModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ("first_name", "last_name", "email", "password")
        extra_kwargs = {
            "password": {
                "write_only": True,
                "min_length": 1
            }
        }

    def create(self, validated_data):
        user = UserModel(
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            email=validated_data["email"]
        )
        user.set_password(validated_data["password"])
        user.save()

        return user


class AuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(
        style={
            "input_tye": "password"
        },
        trim_whitespace=False
    )

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        user = authenticate(
            request=self.context.get("request"),
            email=email,
            password=password
        )
        if not user:
            raise serializers.ValidationError(
                "Unable to authenticate with provided credentials",
                code="authentication"
            )

        attrs["user"] = user
        return attrs
