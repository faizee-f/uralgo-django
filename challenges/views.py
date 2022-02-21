from challenges.models import Challenge, TagList
from challenges.serializers import ChallengeSerializer, TagListSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.paginator import Paginator
from rest_framework import status,generics,mixins
from django.shortcuts import get_object_or_404

# class ChallengeSetPagination(PageNumberPagination):
#     page_size = 10
#     page_size_query_param = 'page_size'
#     max_page_size = 20

# class AddChallenge(generics.CreateAPIView):
#     queryset=Challenge.objects.all()
#     serializer_class=ChallengeSerializer

# class AddChallenge(generics.CreateAPIView):
#     queryset=Challenge.objects.all()
#     serializer_class=ChallengeSerializer


class ChallengeList(APIView):
    def get(self,request):
        challenge=Challenge.objects.filter(is_active=True,report__lt=2)  
        serializer=ChallengeSerializer(challenge,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request):
        serializer=ChallengeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UserChallenge(APIView):
    def get(self,request):
        # user=request.user
        # challenge=Challenge.objects.filter(created_by=user)
        challenge=Challenge.objects.all()
        serializer=ChallengeSerializer(challenge,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class ChallengeDetail(APIView):

    def get(self,request,pk):
        try:
            challenge=Challenge.objects.get(pk=pk)
        except Challenge.DoesNotExist:
            return Response({'error': 'Challenge Not found'},status=status.HTTP_404_NOT_FOUND)
        
        serializer=ChallengeSerializer(challenge)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def put(self,request,pk):
        user=request.user        
        try:
            challenge=Challenge.objects.get(pk=pk)
        except Challenge.DoesNotExist:
            return Response({'error': 'Challenge Not found'},status=status.HTTP_404_NOT_FOUND)
        if challenge.created_by==user:
            serializer=ChallengeSerializer(challenge,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'success': 'Your challenge data has been updated successfully'},serializer.data,status=status.HTTP_202_ACCEPTED)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error':'Unautherized'},status=status.HTTP_401_UNAUTHORIZED)

    def delete(self,request,pk):
        user=request.user        
        try:
            challenge=Challenge.objects.get(id=pk)
            challenge.delete()
            return Response({'success': 'Challenge has been deleted successfully'},status=status.HTTP_204_NO_CONTENT)

        except Challenge.DoesNotExist:
            return Response({'error': 'Challenge Not found'},status=status.HTTP_404_NOT_FOUND)
       

def ReportChallenge(request,pk):
    if request.user.is_authenticated():
        try:
            challenge=Challenge.objects.get(pk=pk)
            challenge.report+=1
            challenge.save()
        except Challenge.DoesNotExist:
            return Response({'error': 'Challenge Not found'},status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({'error':'Unautherized'},status=status.HTTP_401_UNAUTHORIZED)

class TagManager(APIView):
    def get(self, request):
        taglist=TagList.objects.all()  
        serializer=TagListSerializer(taglist,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self, request):
        pass

    def put(self, request,pk):
        pass

    def delete(self, request):
        pass
