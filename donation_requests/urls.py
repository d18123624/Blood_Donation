from .views import SearchOwnModelViewSet,SearchModelViewSet,RequestForDonationModelViewSet,RequestsReceivedOwnModelViewSet
from django.conf.urls import url
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'get_own_searches',SearchOwnModelViewSet)
router.register(r'search',SearchModelViewSet)
router.register(r'request_for_donation',RequestForDonationModelViewSet)
router.register(r'received_requests_own',RequestsReceivedOwnModelViewSet)
urlpatterns=router.urls