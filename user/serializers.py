from rest_framework.serializers import ModelSerializer, SerializerMethodField
from user.models import NewUser
from django.contrib.auth.hashers import make_password


class UserSerializer(ModelSerializer):

    # first_name = SerializerMethodField()

    class Meta:
        model = NewUser
        fields = ['id', 'first_name', 'last_name', 'user_name']

    # def get_first_name(self, obj):
    #     print(obj.id)
    #     return 'outro'


class UserRegisterSerializer(ModelSerializer):
    class Meta:
        model = NewUser
        fields = ('user_name', 'first_name',
                  'last_name', 'password')

    def save(self):
        user = NewUser(
            user_name=self.validated_data['user_name'], first_name=self.validated_data['first_name'], last_name=self.validated_data['last_name'])
        password = self.validated_data['password']
        user.set_password(password)
        user.save()
        return user
