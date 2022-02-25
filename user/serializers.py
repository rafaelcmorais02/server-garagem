from dataclasses import field
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from user.models import NewUser


class UserSerializer(ModelSerializer):

    # first_name = SerializerMethodField()

    class Meta:
        model = NewUser
        fields = ['id', 'first_name', 'last_name', 'user_name']

    # def get_first_name(self, obj):
    #     print(obj.id)
    #     return 'outro'
