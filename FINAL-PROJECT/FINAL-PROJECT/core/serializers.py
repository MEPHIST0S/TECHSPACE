from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Department, Position, Employee
from django.utils import translation
from googletrans import Translator

# Creating serializers for registration and authentication

# Now, let's create serializers for user registration and authentication using JWT. 
# In the core directory, add a file named serializers.py:

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
        
translator = Translator()

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name', 'created_at', 'updated_at']

    def to_representation(self, instance):
        # DISPLAYING NAME DEPENDED ON CURRENT NAME
        representation = super().to_representation(instance)
        lang = translation.get_language()  # GETTING CURRENT NAME
        if lang == 'az':
            representation['name'] = instance.name_az  # DISPLAY AZ
        else:
            representation['name'] = instance.name_en  # DISPLAY ENG
        return representation

    def create(self, validated_data):
        # GETTING NAME
        name = validated_data.get('name', '')
        
        if not name:
            raise serializers.ValidationError("Name field cannot be empty.")
        
        # GETTING CURRENT LANGUAGE
        lang = translation.get_language()

        # TRANSLATION LOGIC
        if lang == 'az':
            validated_data['name_az'] = name
            translated_name = translator.translate(name, dest='en').text  # TRANSLATION TO ENG
            validated_data['name_en'] = translated_name
        else:
            validated_data['name_en'] = name
            translated_name = translator.translate(name, dest='az').text  # TRANSLATION TO AZ
            validated_data['name_az'] = translated_name

        # CREATION NEW DEPARTMENT
        department = Department.objects.create(**validated_data)
        return department

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ['id', 'name', 'salary', 'department', 'created_at', 'updated_at']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        lang = translation.get_language()  # Get the current language
        print(f"Current Language: {lang}")  # Debug print to check the language
        if lang == 'az':
            representation['name'] = instance.name_az  # Use Azerbaijani name
        else:
            representation['name'] = instance.name_en  # Use English name
        return representation

    def create(self, validated_data):
        # Same create logic as before
        name = validated_data.get('name', '')
        
        if not name:
            raise serializers.ValidationError("Name field cannot be empty.")
        
        lang = translation.get_language()

        # TRANSLATION LOGIC
        if lang == 'az':
            validated_data['name_az'] = name  # Set Azerbaijani name
            translated_name = translator.translate(name, dest='en').text  # TRANSLATION TO EN
            validated_data['name_en'] = translated_name  # Set English name
        else:
            validated_data['name_en'] = name  # Set English name
            translated_name = translator.translate(name, dest='az').text  # TRANSLATION TO AZ
            validated_data['name_az'] = translated_name  # Set Azerbaijani name

        # CREATION NEW POSITION
        position = Position.objects.create(**validated_data)
        return position

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'surname', 'email', 'department', 'position', 'status', 'created_at', 'updated_at']