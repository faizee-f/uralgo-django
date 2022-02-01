from django.shortcuts import render
from accounts.models import Account
from api.serializers import AccountSerializer, MyTokenObtainPairSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics,mixins
from rest_framework.decorators import api_view, permission_classes
from rest_framework import authentication, permissions
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



class RegisterUser(generics.CreateAPIView):
    queryset=Account.objects.all()
    serializer_class=AccountSerializer


@permission_classes((permissions.AllowAny,))
class AccountList(APIView):

    

    def get(self,request):
        accounts=Account.objects.all()
        serializer=AccountSerializer(accounts,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer=AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@permission_classes((permissions.AllowAny,))
class AccountDetail(APIView):

    def get(self,request,pk):
        try:
            account=Account.objects.get(pk=pk)
        except Account.DoesNotExist:
            return Response({'error': 'Account Not found'},status=status.HTTP_404_NOT_FOUND)
        
        serializer=AccountSerializer(account)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def put(self,request,pk):
        account=Account.objects.get(pk=pk)
        serializer=AccountSerializer(account,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': 'Your data has been updated successfully'},serializer.data,status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        account=Account.objects.get(id=pk)
        account.delete()
        return Response({'success': 'User has been deleted successfully'},status=status.HTTP_204_NO_CONTENT)


