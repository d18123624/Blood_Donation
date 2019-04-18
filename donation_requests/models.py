from django.db import models
from person.models import Person
# Create your models here.

class Search(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    search_person=models.ForeignKey(to=Person,on_delete=models.CASCADE,related_name='person_search',blank=True,null=True) # People can search without logging in
    search_lat = models.DecimalField(max_digits=22, decimal_places=16, blank=False, null=False)
    search_long = models.DecimalField(max_digits=22, decimal_places=16, blank=False, null=False)
    search_max_distance_metres=models.DecimalField(max_digits=8,decimal_places=0,blank=False,null=False)
    no_of_matches=models.IntegerField(null=False,blank=False)
    blood_group_patient = models.CharField(max_length=3, choices=(
        ('O+', 'O Positive'),
        ('O-', 'O Negative'),
        ('A+', 'A Positive'),
        ('A-', 'A Negative'),
        ('B+', 'B Positive'),
        ('B-', 'B Negative'),
        ('AB+', 'AB Positive'),
        ('AB-', 'AB Negative'),
    ), blank=False, null=False)


class SearchMatches(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    search_match=models.ForeignKey(to=Search,on_delete=models.CASCADE,related_name='search_match')
    match_person=models.ForeignKey(to=Person,on_delete=models.CASCADE,related_name='person_match')
    distance_in_metres=models.DecimalField(max_digits=8,decimal_places=0,blank=True,null=True)
    search_criteria_met=models.BooleanField(blank=False,null=False)


class RequestForDonation(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    person_donation_request=models.ForeignKey(Person,on_delete=models.CASCADE,related_name='person_donation_request')
    search_match_donation=models.ForeignKey(SearchMatches,on_delete=models.CASCADE,related_name='donation_search_match')
