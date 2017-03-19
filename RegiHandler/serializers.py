from django.contrib.auth.models import User, Group
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

from RegiHandler.models import DolbyUser
from rest_framework import serializers

# user group
client_group = Group.objects.get(name = 'client')
admin_group = Group.objects.get(name = 'admin')

# email validator
def EmailValidator(email):
    try:
        validate_email(email)
    except ValidationError:
        raise serializers.ValidationError('invalid email')

class DolbyUserSerializer(serializers.Serializer):
    # # basic filed from django User
    username = serializers.CharField()
    password = serializers.CharField()
    email = serializers.EmailField(validators = [EmailValidator])
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
    
    """
    record creation api                                  <br/>
    status code: {                                       <br/>
        200: success creating user                       <br/>
        301: user already exist, return existing record  <br/>
        402: email already exist, return existing record <br/>
    }
    @return (user, status_code)
    @param validated_data    [in]    rest_framework serializers validated_data object
    """
    def create(self, validated_data):
        # check if username is already exist first
        try:
            user = User.objects.get(username = validated_data.get('username'))
            return user, 301
        except User.DoesNotExist:
            # check duplicate email second
            try:
                user = User.objects.get(email = validated_data.get('email'))
                return user, 402
            except User.DoesNotExist:
                # create basic user model
                user = User(
                    username = validated_data.get('username'),
                    email = validated_data.get('email'),
                    first_name = validated_data.get('first_name', None), # not required
                    last_name = validated_data.get('last_name', None)    # not required
                )
                # force password hashing
                user.set_password(validated_data.get('password'))
                user.save()
                # get DolbyUser data
                dolbyuser_data = validated_data.get('dolbyuser')
                # create meta data profile
                dlb_user = DolbyUser(
                    user = user,
                    company = dolbyuser_data.get('company'),
                    registration_code = dolbyuser_data.get('registration_code'),
                    phone_number = dolbyuser_data.get('phone_number')
                )
                dlb_user.save()

                # check email and company for admin permission
                # granted permission for Dolby Laboratory user with @dolby.com email address
                if (
                    dlb_user.company == 'dolby laboratories' and 
                    user.email[user.email.find('@'):] == '@dolby.com'
                   ):
                    # grant admin group permission
                    user.groups.add(admin_group)
                    # grant staff access permission
                    user.is_staff = True
                    user.save()
                else:
                    user.groups.add(client_group)
                
                return user, 200
    
    """
    record update api                                    <br/>
    status code: {                                       <br/>
        201: success updating user                       <br/>
    }
    @return (user, status_code)
    @param instance          [in]    instance of user for update
    @param validated_data    [in]    rest_framework serializers validated_data object
    """
    def update(self, instance, validated_data):
        # update password
        self.update_helper(instance, 'password', validated_data)
        # update email
        self.update_helper(instance, 'email', validated_data)
        # update name
        self.update_helper(instance, 'first_name', validated_data)
        self.update_helper(instance, 'last_name', validated_data)
        # update phone number
        self.update_helper(instance, 'phone_number', validated_data, is_dolby = True)
        # update profile first
        instance.dolbyuser.save()
        # update info last
        instance.save()
        return instance, 201
    
    """
    update helper
    """
    def update_helper(self, instance, key, validated_data, is_dolby = False):
        if validated_data.get(key, None) is not None:
            if key == 'password':
                instance.set_password(validated_data.get('password')) 
            else:
                if is_dolby:
                    setattr(instance.dolbyuser, key, validated_data(key))
                else:
                    setattr(instance, key, validated_data.get(key))

    """
    record create/update api                             <br/>
    status code: {                                       <br/>
        200: success creating user                       <br/>
        201: success updating user                       <br/>
    }
    @return (user, status_code)
    @param validated_data    [in]    rest_framework serializers validated_data object
    """
    def create_or_update(self, validated_data):
        # record exist
        try:
            return self.update(
                User.objects.get(username = validated_data.get('username')), 
                validated_data
            )
        except User.DoesNotExist:
            return self.create(validated_data)