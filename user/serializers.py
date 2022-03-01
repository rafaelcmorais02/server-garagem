from rest_framework.serializers import ModelSerializer, SerializerMethodField, ValidationError
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
                  'last_name', 'password', 'password2')

    def save(self):
        user = NewUser(
            user_name=self.validated_data['user_name'], first_name=self.validated_data['first_name'], last_name=self.validated_data['last_name'])
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise ValidationError(
                {'password': 'As senhas devem ser iguais'})
        user.set_password(password)
        user.save()
        return user
