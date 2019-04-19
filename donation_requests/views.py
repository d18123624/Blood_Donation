import pandas as pd
from django.shortcuts import render
from rest_framework import views,viewsets
from rest_framework.views import APIView,status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets,mixins

from person.models import Person
from .models import RequestForDonation,Search,SearchMatches
from .serializers import SearchSerializer,RequestForDonationModelSerializer
import requests
from blood_donor.credentials import GOOGLE_MAPS_API_KEY
from blood_donor.settings import BASE_DIR
import json
from django.db.models import Q
# Create your views here.

class SearchOwnModelViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Search.objects.all()
    serializer_class = SearchSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user=self.request.user
        return Search.objects.filter(search_person=user.person)

class SearchModelViewSet(viewsets.GenericViewSet,mixins.CreateModelMixin):

    queryset = Search.objects.all()
    serializer_class = SearchSerializer

    @classmethod
    def get_distance_from_google_maps(cls,search_obj,QUERY_POINTS_LIMIT_GOOGLE=24):
        source_point=(search_obj.search_lat,search_obj.search_long)
        blood_group_patient=search_obj.blood_group_patient
        with open('{}/donation_requests/recipient_donor_dependency.json'.format(BASE_DIR),'r') as f:
            recipient_donor_dependency=json.loads(f.read())
        possible_donor_blood_groups=recipient_donor_dependency[blood_group_patient]
        for i,blood_type in enumerate(possible_donor_blood_groups):
            if i==0:
                query_filter=Q(blood_group=blood_type)
            else:
                query_filter=query_filter|Q(blood_group=blood_type)
        if search_obj.search_person:
            exclude_kwargs={'id':search_obj.search_person.id}
        else:
            exclude_kwargs={}
        destination_points_df=pd.DataFrame.from_records(Person.objects.filter(query_filter,currently_eligible_for_donation=True).exclude(**exclude_kwargs).values('id','address_lat','address_long'))
        #destination_points_df
        #criteria_distance=
        maps_url='https://maps.googleapis.com/maps/api/distancematrix/json'
        no_of_matches=0
        df_len=destination_points_df.shape[0]
        #result_points=[]
        criteria_distance_in_metres=search_obj.search_max_distance_metres
        for i in range(0,df_len,QUERY_POINTS_LIMIT_GOOGLE):
            lower_limit=i
            upper_limit=min(i+QUERY_POINTS_LIMIT_GOOGLE,df_len)
            destination_points_df_extract=destination_points_df.iloc[lower_limit:upper_limit]
            r=requests.get(url=maps_url,params={'key':GOOGLE_MAPS_API_KEY,'units':'metric','origins':'{},{}'.format(*source_point),'destinations':'|'.join(['{},{}'.format(x['address_lat'],x['address_long']) for _,x in destination_points_df_extract.iterrows()])})
            print(r.url)
            if r.status_code==200:
                resp=r.json()
                resp_elements=resp['rows'][0]['elements']
                for j,each in enumerate(resp_elements):
                    # if each['status']=='OK' and each['distance']['value']<=criteria_distance_in_metres:
                    #     result_points.append([destination_points_df_extract.iloc[j]['person_id'],destination_points_df_extract.iloc[j]['latitude'],destination_points_df_extract.iloc[j]['longitude'],each['distance']['value']])
                    searchmatch_obj=SearchMatches.objects.create(search_match=search_obj,match_person=Person.objects.get(id=destination_points_df_extract.iloc[j]['id']),distance_in_metres=each['distance']['value'] if each['status']=='OK' else None,search_criteria_met=each['distance']['value']<=criteria_distance_in_metres if each['status']=='OK' else False)
                    if searchmatch_obj.search_criteria_met:
                        no_of_matches+=1
                    searchmatch_obj.save()
            else:
                return None
            return no_of_matches

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data,context={'request':request,'no_of_matches':0})
        serializer.is_valid(raise_exception=True)
        search_model_obj=serializer.save()
        no_of_matches=self.get_distance_from_google_maps(search_model_obj)
        if no_of_matches is None:
            search_model_obj.delete()
            return Response({"error":True,"message":"Internal Server Error...Try Again!!!"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            headers = self.get_success_headers(serializer.data)
            search_model_obj.no_of_matches=no_of_matches
            search_model_obj.save()
            #Since no_of_matches is being updated later, so reinitializing the serializer
            serializer=self.get_serializer(search_model_obj)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class RequestForDonationModelViewSet(viewsets.GenericViewSet,mixins.CreateModelMixin,mixins.ListModelMixin):

    queryset = RequestForDonation.objects.all()
    serializer_class = RequestForDonationModelSerializer
    permission_classes = (IsAuthenticated,)

    # def get_queryset(self):
    #     user=self.request.user
    #     return RequestForDonation.objects.filter(person_donation_request=user.person)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data,context={'request':request})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class RequestsReceivedOwnModelViewSet(viewsets.GenericViewSet,mixins.ListModelMixin):
    queryset = RequestForDonation.objects.all()
    serializer_class = RequestForDonationModelSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return RequestForDonation.objects.filter(search_match_donation__match_person=self.request.user.person)

