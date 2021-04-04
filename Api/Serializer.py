from rest_framework import serializers
from Netflix.models.Show import Show
from django.contrib.auth.models import User

# from Netflix.models.User import User


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
        model = User
        exclude =  ['password',]



class RegistrationSerilalizer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username','email','password','password2']

    def save(self, **kwargs):
        user = User(email=self.validated_data.get('email'),
                    username= self.validated_data.get('username')
        )

        if self.validated_data.get('password') !=  self.validated_data.get('password2'):
            raise serializers.ValidationError(
                {
                    'password': "Password doesn't match"
                }
            )
        else:
            user.set_password(self.validated_data.get('password'))
            user.save()

# class RegistrationSerilalizer(serializers.ModelSerializer):
#     password2 = serializers.CharField(write_only=True)
#     class Meta:
#         model = User
#         # fields = ['firstName','lastName','email','password','password2']
#         fields = '__all__'
#         execlude = ['password','password2']
#         extra_kwargs = {
#             'password':{'write_only':True}
#         }

#     def save(self):
#         user = User(
#             firstName= self.validated_data['firstName'],
#             lastName= self.validated_data['lastName'],
#             email =  self.validated_data['email'],
#         )

#         password = self.validated_data['password']
#         password2 = self.validated_data['password2']

#         if password != password2:
#             raise serializers.ValidationError({
#                 'password' : "Password Doesn't Match"
#             })
#         user.set_password(self.validated_data.get('password'))
#         user.save()
#         return user




