from .views import SignUp,OwnPersonView
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
router=DefaultRouter()
router.register(r'own_info',OwnPersonView)
urlpatterns=router.urls
urlpatterns.append(url(r'^signup/$',SignUp.as_view()))
urlpatterns.append(url(r'^login/', views.obtain_auth_token))
