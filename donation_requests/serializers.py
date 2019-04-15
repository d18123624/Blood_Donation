from rest_framework import serializers
from .models import SearchMatches,Search,RequestForDonation
from person.models import Person
from django.contrib.auth.models import User,AnonymousUser
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.serializers import ValidationError
from .utils import distance_to_metres


class SearchMatchesLoggedInSerializer(serializers.ModelSerializer):

    class Meta:
        model=SearchMatches
        #fields='__all__'
        exclude=('search_match',)
        depth=1


class SearchMatchesNotLoggedInSerializer(serializers.ModelSerializer):
    latitude=serializers.ReadOnlyField(source="match_person.address_lat")
    longitude = serializers.ReadOnlyField(source="match_person.address_long")
    blood_group=serializers.ReadOnlyField(source="match_person.blood_group")

    class Meta:
        model=SearchMatches
        fields=('distance_in_metres','blood_group','latitude','longitude',)

class SearchSerializer(serializers.ModelSerializer):
    person_matches=serializers.SerializerMethodField(read_only=True)

    class Meta:
        model=Search
        fields=('search_lat','search_long','search_max_distance_metres','search_person','no_of_matches','blood_group_patient','person_matches',)
        #TODO: In the front end, prefill this with the patient's own blood group and then allow him/her to change if needed
        read_only_fields=('search_person','no_of_matches','person_matches',)
        depth=1

    def validate_search_max_distance_metres(self,val):
        if val<0:
            raise serializers.ValidationError("This should be positive")
        return val

    def get_person_matches(self,obj):
        user=self.context['request'].user
        if user.is_authenticated:
            serializer_obj=SearchMatchesLoggedInSerializer(obj.search_match.filter(search_criteria_met=True),many=True)
            return serializer_obj.data
        else:
            serializer_obj=SearchMatchesNotLoggedInSerializer(obj.search_match.filter(search_criteria_met=True),many=True)
            return serializer_obj.data

    def create(self, validated_data):
        request=self.context['request']
        no_of_matches=self.context.get('no_of_matches',0) #TODO: Check why no_of_matches not appearing in context
        model_obj=self.Meta.model.objects.create(search_person=request.user.person if request.user.is_authenticated else None,no_of_matches=no_of_matches,**validated_data)
        model_obj.save()
        return model_obj


class RequestForDonationModelSerializer(serializers.ModelSerializer):
    search_match_donation_id=serializers.IntegerField(write_only=True)
    class Meta:
        model=RequestForDonation
        fields=('created_at','person_donation_request','search_match_donation_id','search_match_donation',)
        read_only_fields = ('created_at','person_donation_request','search_match_donation',)
        depth=1

    # def validate(self, attrs):
    #     errors = dict()
    #     request=self.context['request']
    #     if request.user.person != SearchMatches.objects.get(id=attrs['search_match_id']).search_match.search_person:
    #         errors['search_match']='Request for Donation can only be made by the same person who searched!'
    #         if errors:
    #             raise serializers.ValidationError(errors)
    #     return attrs

    def validate_search_match_donation_id(self, val):
        request=self.context['request']
        if request.user.person != SearchMatches.objects.get(id=val).search_match.search_person:
            raise serializers.ValidationError("Request for Donation can only be made by the same person who searched!")
        if RequestForDonation.objects.filter(person_donation_request=request.user.person,search_match_donation_id=val).exists():
            raise serializers.ValidationError("A Request For Donation by the same person for the same match already exists!!!")
        return val


    def create(self, validated_data):
        request=self.context['request']
        model_obj=self.Meta.model.objects.create(person_donation_request=request.user.person,**validated_data)
        model_obj.save()
        return model_obj