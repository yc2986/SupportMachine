from django.contrib.auth.models import User

from RegiHandler.models import DolbyUser
from rest_framework import serializers

class DolbyUserSerializer(serializers.Serializer):
    # # basic filed from django User
    username = serializers.CharField()
    password = serializers.CharField()
    email = serializers.EmailField()
    first_name = serializers.CharField(required = False, allow_blank = True, allow_null = True)
    last_name = serializers.CharField(required = False, allow_blank = True, allow_null = True)
    # extra field from DolbyUser
    company = serializers.CharField(source = 'dolbyuser.company')
    registration_code = serializers.CharField(source = 'dolbyuser.registration_code')
    phone_number = serializers.CharField(source = 'dolbyuser.phone_number')

    class Meta:
        model = User
        fields = (
            'username', 'email', 'password', 
            'company', 'registration_code', 
            'first_name', 'last_name', 'phone_number'
        )

    
    def create(self, validated_data):
        # create basic user model
        user = User(
            username = validated_data.get('username'),
            email = validated_data.get('email'),
            password = validated_data.get('password'),
            first_name = validated_data.get('first_name', None), # not required
            last_name = validated_data.get('last_name', None)    # not required
        )
        user.save()
        # create meta data profile
        dlb_user = DolbyUser(
            user = user,
            company = validated_data.get('company'),
            registration_code = validated_data.get('registration_code'),
            phone_number = validated_data.get('phone_number')
        )
        dlb_user.save()
        return user
    
    def update(self, instance, validated_data):
        # query record by username (unique)
        user = User.objects.get(username = validated_data.get('username'))
        # update password
        user.set_password(validated_data.get('password')) 
        # update email
        user.email = validated_data.get('email')
        # update name
        if validated_data.get('first_name', None) is not None:
            user.email = validated_data.get('first_name')
        if validated_data.get('last_name', None) is not None:
            user.email = validated_data.get('last_name')
        # update phone number
        user.dolbyuser.phone_number = validated_data.get('phone_number')
        # update profile first
        user.dolbyuser.save()
        # update info last
        user.save()
        return user

    def create_or_update(self, validated_data):
        # record exist
        try:
            return self.update(
                User.objects.get(user = validated_data.get('username')), 
                validated_data
            )
        except User.DoesNotExist:
            return self.create(validated_data)