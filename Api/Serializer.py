from rest_framework import serializers
from Netflix.models.Show import Show
from Netflix.models.Profile import Profile, WatchLater, Watched
from django.core import exceptions
import django.contrib.auth.password_validation as validators


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
    country = serializers.StringRelatedField()
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
            avatar =  self.validated_data['avatar'],
            membership =  self.validated_data['membership'],
            payment_day =  self.validated_data['payment_day'],
            membership_Start_Date =  self.validated_data['membership_Start_Date'],
        )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        try:
            (validators.validate_password(password) != None)
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({
                "error":e
            })
        else:
            if password != password2:
                raise serializers.ValidationError({
                    'password' : "Password Doesn't Match"
                })

        user.set_password(password)
        user.save()
        return user


class WatchLaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchLater
        fields = ['Show_id', 'User_id']

class WatchedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watched
        fields =['Show_id','User_id']

