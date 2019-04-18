from .models import Person
from django.contrib.auth.models import User
from rest_framework.serializers import Serializer
from rest_framework import serializers
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.serializers import ValidationError
import django.contrib.auth.password_validation as validators
import datetime
from rest_framework.serializers import ModelSerializer

class PersonCreateSerializer(Serializer):
    username=serializers.CharField(max_length=100,allow_blank=False,allow_null=False)
    password=serializers.CharField(max_length=100,allow_blank=False,allow_null=False)
    email=serializers.EmailField(allow_null=True,allow_blank=True,required=False)
    name=serializers.CharField(max_length=100,allow_blank=False,allow_null=False)
    age=serializers.IntegerField(max_value=120,min_value=17,allow_null=False)
    gender=serializers.CharField(max_length=1,allow_null=False,allow_blank=False)
    blood_group=serializers.CharField(max_length=2,allow_null=False,allow_blank=False)
    address_lat=serializers.DecimalField(max_digits=22,decimal_places=16,allow_null=False,min_value=-90,max_value=90)
    address_long=serializers.DecimalField(max_digits=22,decimal_places=16,allow_null=False,min_value=-180,max_value=180)
    mobile_number=serializers.DecimalField(max_digits=13,decimal_places=0,allow_null=False)
    last_blood_donation=serializers.DateField(allow_null=True)
    currently_eligible_for_donation=serializers.BooleanField(allow_null=False)


    def validate_username(self,value):
        try:
            User.objects.get(username=value)
        except ObjectDoesNotExist as e:
            return value
        raise ValidationError("Username already exists!")

    def validate_password(self,value):
        validators.validate_password(value)
        return value

    def validate_email(self, value):
        try:
            User.objects.get(email=value)
        except ObjectDoesNotExist:
            return value
        raise serializers.ValidationError("Email Exists")

    def validate_gender(self,value):
        if value in {'M','F','O'}:
            return value
        raise serializers.ValidationError("Gender should be Male(M), Female(F) or Other(O)")

    def validate_blood_group(self,value):
        if value in {'O+','O-','A+','A-','B+','B-','AB+','AB-'}:
            return value
        raise serializers.ValidationError("Invalid Blood Group")

    def validate(self,attrs):
        errors=dict()
        if 'last_blood_donation' in attrs and attrs['last_blood_donation']:
            if attrs['last_blood_donation']>datetime.date.today():
                errors['last_blood_donation']='Last Blood Donation date is in the future!'
            elif attrs['currently_eligible_for_donation'] and (datetime.date.today()-attrs['last_blood_donation']).days<56:
                errors['currently_eligible_for_donation']='You have to wait atleast 56 days from your last date of blood donation...so please set this option to No as of now!'
        if errors:
            raise serializers.ValidationError(errors)
        return attrs

    def create(self, validated_data):
        user_fields={'username','password','email'}
        user_obj_args={k:v for k,v in validated_data.items() if k in user_fields}
        user=User.objects.create_user(**user_obj_args)
        user.save()
        person_obj_args={k:v for k,v in validated_data.items() if k not in user_fields}
        person_obj=Person(user=user,**person_obj_args)
        person_obj.save()
        return person_obj

    def update(self, instance, validated_data):
        raise NotImplementedError # since i dont plan on using it


class PersonModelSerializer(ModelSerializer):
    username = serializers.SerializerMethodField(read_only=True)
    email=serializers.SerializerMethodField(read_only=True)

    def get_username(self,obj):
        return obj.user.username

    def get_email(self,obj):
        return obj.user.email

    class Meta:
        model=Person
        fields=('username','email','created_at','modified_at','name','age','gender','blood_group','address_lat','address_long','mobile_number','last_blood_donation','currently_eligible_for_donation',)


class PersonUpdateSerializer(ModelSerializer):
    last_blood_donation = serializers.DateField(allow_null=True)
    currently_eligible_for_donation = serializers.BooleanField(allow_null=False)

    class Meta:
        model=Person
        fields=('last_blood_donation','currently_eligible_for_donation',)

    def update(self, instance, validated_data):
        for key in validated_data:
            setattr(instance,key,validated_data[key])
        instance.save()
        return instance

    def validate(self, attrs):
        errors = dict()
        if 'last_blood_donation' in attrs and attrs['last_blood_donation']:
            if attrs['last_blood_donation'] > datetime.date.today():
                errors['last_blood_donation'] = 'Last Blood Donation date is in the future!'
            elif attrs['currently_eligible_for_donation'] and (
                    datetime.date.today() - attrs['last_blood_donation']).days < 56:
                errors[
                    'currently_eligible_for_donation'] = 'You have to wait atleast 56 days from your last date of blood donation...so please set this option to No as of now!'
        if errors:
            raise serializers.ValidationError(errors)
        return attrs

