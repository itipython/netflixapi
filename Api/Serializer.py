from rest_framework import serializers
from Netflix.models.Show import Show
from Netflix.models.Profile import Profile
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class ShowSerializer(serializers.ModelSerializer):
    authors = serializers.StringRelatedField(many=True)
    genres = serializers.StringRelatedField(many=True)
    directors = serializers.StringRelatedField(many=True)
    producers = serializers.StringRelatedField(many=True)
    actors = serializers.StringRelatedField(many=True)
    prizes = serializers.StringRelatedField()

    class Meta:
        model = Show
        fields = '__all__'
      


class UserSerializer(serializers.ModelSerializer):
    membership = serializers.StringRelatedField()
    class Meta:
        model = Profile
        exclude =  ['password',]

class RegistrationSerilalizer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only= True)
    class Meta:
        model = Profile
        fields = ['first_name','last_name','email','password','password2','phone','country','birth_date'
        ,'gender','register_date','avatar','payment','membership_Start_Date']

        extra_kwargs = {
            'password':{'write_only':True},
        }

    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({
                'password' : "Password Doesn't Match"
            })
        user = Profile.objects.create(
            first_name= self.validated_data['first_name'],
            last_name= self.validated_data['last_name'],
            password=self.validated_data['password'],
            email = self.validated_data['email'],
            phone =  self.validated_data['phone'],
            country =  self.validated_data['country'],
            birth_date =  self.validated_data['birth_date'],
            gender =  self.validated_data['gender'],
            register_date =  self.validated_data['register_date'],
            avatar =  self.validated_data['avatar'],
            # membership =  self.validated_data['membership'],
            payment =  self.validated_data['payment'],
            membership_Start_Date =  self.validated_data['membership_Start_Date'],
        )
        return user




