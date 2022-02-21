from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Challenge, TagList


 
class TagListSerializer(serializers.ModelSerializer):
    class Meta:
        model=TagList
        fields=['tag']

       
class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = ['created_by','question','difficulty','likes','tags','caseInput','caseOutput','is_active']