from django.urls import path,include
from accounts.views import AccountDetail, AccountList, RegisterUser,MyTokenObtainPairView


urlpatterns=[
    path('signup/',RegisterUser.as_view(),name='register_user'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('verification/', include('verify_email.urls')),

    path('account_list/',AccountList.as_view(),name='account_list'),
    path('account_list/<int:pk>/',AccountDetail.as_view(),name='account_details'),
]