from accounts.models import Account
from rest_framework import serializers
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['email'] = user.email
        token['full_name']=user.full_name()
        token['is_admin']= user.is_admin
        token['is_active']= user.is_active
        # ...

        return token


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model=Account
        fields = ("first_name", "last_name", "email", "password")
        extra_kwargs = {
            "first_name": {"required": True},
            "last_name": {"required": True},
            "email": {"required": True},
            "password":{'write_only':True,'required':True}
        }

    # field level validation
    def validate_first_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Name is too short")
        else:
            return value


    def validate(self, data):
        if Account.objects.filter(email=data["email"]):
            raise serializers.ValidationError({"email": "Email already exist"})
        return data

    def create(self, validated_data):
        
        user = Account.objects.create_user(
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            password=validated_data["password"],
        )
        user.set_password(validated_data["password"])
        user.save()
        
        return user