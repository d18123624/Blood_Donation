from django.shortcuts import render
from rest_framework.views import APIView,status
from .serializers import PersonCreateSerializer, PersonModelSerializer, PersonUpdateSerializer
from .models import Person
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import viewsets,mixins
# Create your views here.

class SignUp(APIView):

    def post(self,request):
        person_create_serializer=PersonCreateSerializer(data=request.data.dict())
        if person_create_serializer.is_valid():
            person_obj=person_create_serializer.save()
            read_serializer=PersonModelSerializer(person_obj,context={'request':request})
            token_obj=Token.objects.create(user=person_obj.user)
            return Response({'error':False,'message':'User created and logged in successfully!','token':token_obj.key,'person':read_serializer.data})
        else:
            return Response({'error':True,'error_fields':person_create_serializer.errors,'message':'Error Occured!'},status=status.HTTP_400_BAD_REQUEST)


class OwnPersonView(viewsets.GenericViewSet,mixins.ListModelMixin):
    # For retrieving the logged in account details
    serializer_class = PersonModelSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Person.objects.all()

    def get_queryset(self):
        user=self.request.user
        return Person.objects.filter(user=user)

class LogOutView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self,request):
        token_obj=Token.objects.get(user=request.user)
        token_obj.delete()
        return Response({'error':False,'message':'Logged out successfully!'})


class DeleteAccountView(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self,request):
        token_obj=Token.objects.get(user=request.user)
        token_obj.delete()
        request.user.delete()
        return Response({'error':False,'message':'Account Deleted Successfully!'})


class UpdateAccountView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self,request):
        person_obj=request.user.person
        person_update_serializer = PersonUpdateSerializer(person_obj,data=request.data.dict())
        if person_update_serializer.is_valid():
            person_obj = person_update_serializer.save()
            read_serializer = PersonModelSerializer(person_obj, context={'request': request})
            return Response(
                {'error': False, 'message': 'Information updated successfully!',
                 'person': read_serializer.data})
        else:
            return Response(
                {'error': True, 'error_fields': person_update_serializer.errors, 'message': 'Error Occured!'},status=status.HTTP_400_BAD_REQUEST)

