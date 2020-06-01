from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from .models import User
from allauth.account.adapter import get_adapter
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'email', 'username', 'password', 'is_farmer', 'is_general', 'is_scientist', 'is_government', 'is_admin',
            'is_supplier')


class CustomRegisterSerializer(RegisterSerializer):
    is_farmer = serializers.BooleanField(default=False)
    is_general = serializers.BooleanField(default=True)
    is_scientist = serializers.BooleanField(default=False)
    is_government = serializers.BooleanField(default=False)
    is_admin = serializers.BooleanField(default=False)
    is_supplier = serializers.BooleanField(default=False)

    class Meta:
        model = User
        fields = (
            'email', 'username', 'password', 'is_farmer', 'is_general', 'is_scientist', 'is_government', 'is_admin',
            'is_supplier')

    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'email': self.validated_data.get('email', ''),
            'is_farmer': self.validated_data.get('is_farmer', ''),
            'is_general': self.validated_data.get('is_general', ''),
            'is_scientist': self.validated_data.get('is_scientist', ''),
            'is_government': self.validated_data.get('is_government', ''),
            'is_admin': self.validated_data.get('is_admin', ''),
            'is_supplier': self.validated_data.get('is_supplier', ''),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user.is_farmer = self.cleaned_data.get('is_farmer')
        user.is_general = self.cleaned_data.get('is_general')
        user.is_scientist = self.cleaned_data.get('is_scientist')
        user.is_government = self.cleaned_data.get('is_government')
        user.is_admin = self.cleaned_data.get('is_admin')
        user.is_supplier = self.cleaned_data.get('is_supplier')
        user.save()
        adapter.save_user(request, user, self)

        return user


# overriding token serializers to include other fields
class TokenSerializer(serializers.ModelSerializer):
    user_type = serializers.SerializerMethodField()

    class Meta:
        model = Token
        fields = ('key', 'user', 'user_type')

    def get_user_type(self, obj):
        serializer_data = UserSerializer(
            obj.user
        ).data
        is_farmer = serializer_data.get('is_farmer')
        is_general = serializer_data.get('is_general')
        is_scientist = serializer_data.get('is_scientist')
        is_government = serializer_data.get('is_government')
        is_admin = serializer_data.get('is_admin')
        is_supplier = serializer_data.get('is_supplier')
        return {
            'is_farmer': is_farmer,
            'is_general': is_general,
            'is_scientist': is_scientist,
            'is_government': is_government,
            'is_admin': is_admin,
            'is_supplier': is_supplier

        }
