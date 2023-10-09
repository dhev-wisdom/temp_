from .models import Trader
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

class TraderSerializer(ModelSerializer):
    class Meta:
        model = Trader
        fields = '__all__'

    def get_profit(self, obj):
        return obj.calculate_profit()

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user