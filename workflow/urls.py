from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [

    path('auth/register/',Signup.as_view(),name='check'),
     path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
     path('anime/search/',AniListSearch.as_view(),name='animesearch'),
     path('user/prefrence/',Prefrence.as_view(),name='prefrence'),
     path('anime/recommendations/',Suggestion.as_view(),name='suggestion')
]
