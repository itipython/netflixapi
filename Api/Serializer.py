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
      


class ProfileSerializer(serializers.ModelSerializer):
    membership = serializers.StringRelatedField()
    class Meta:
        model = Profile
        exclude =  ['date_joined','password',"last_login", "is_superuser","is_staff","is_active", "groups","user_permissions"]

class RegistrationSerilalizer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only= True)
    class Meta:
        model = Profile
        fields = ['username','first_name','last_name','email','password','password2','phone','country','birth_date'
        ,'gender','avatar','membership','payment_day','membership_Start_Date']

        extra_kwargs = {
            'password':{'write_only':True},
        }

    def save(self):
        user = Profile(
            username = self.validated_data['username'],
            first_name= self.validated_data['first_name'],
            last_name= self.validated_data['last_name'],
            email = self.validated_data['email'],
            phone =  self.validated_data['phone'],
            country =  self.validated_data['country'],
            birth_date =  self.validated_data['birth_date'],
            gender =  self.validated_data['gender'],
            # register_date =  self.validated_data['register_date'],
            avatar =  self.validated_data['avatar'],
            membership =  self.validated_data['membership'],
            payment_day =  self.validated_data['payment_day'],
            membership_Start_Date =  self.validated_data['membership_Start_Date'],
        )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if len(password) < 8:
            raise serializers.ValidationError({
                'password' : "Password must be at least 8 chars"
            })
        elif password != password2:
            raise serializers.ValidationError({
                'password' : "Password Doesn't Match"
            })
 
        user.set_password(password)
        user.save()
        return user




