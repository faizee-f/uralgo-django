from challenges.models import Challenge
from challenges.serializers import ChallengeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.paginator import Paginator
from rest_framework import status,generics,mixins


class ChallengeSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 20

class AddChallenge(generics.CreateAPIView):
    queryset=Challenge.objects.all()
    serializer_class=ChallengeSerializer

class AddChallenge(generics.CreateAPIView):
    queryset=Challenge.objects.all()
    serializer_class=ChallengeSerializer




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