from django.contrib.auth.models import User, Group
from rest_framework import serializers



class EmailLoginSerialzers(serializers.Serializer):
    """  """
    EmailID = serializers.CharField(required=True)
    Password = serializers.CharField(required=True)

    class Meta:
        fields = '__all__'

class SignupSerialzers(serializers.Serializer):
    """  """
    Name = serializers.CharField(required=True)
    EmailID = serializers.CharField(required=True)
    Password = serializers.CharField(required=True)
    class Meta:
        fields = '__all__'

class UploadFileSerialzers(serializers.Serializer):
    """  """
    #File = serializers.FileField(required=False,allow_blank=True,allow_null=True)
    File = serializers.FileField(required=True)
    EmailID = serializers.CharField(required=True)
    
    class Meta:
        fields = '__all__'