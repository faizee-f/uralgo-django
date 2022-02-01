from django.urls import path
from api.views import AccountDetail, AccountList, RegisterUser,MyTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns=[
    path('signup/',RegisterUser.as_view(),name='register_user'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


    path('account_list/',AccountList.as_view(),name='account_list'),
    path('account_list/<int:pk>/',AccountDetail.as_view(),name='account_details'),
]