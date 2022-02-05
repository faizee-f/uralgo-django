from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Cases, Challenge, Tags



class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = ['question','difficulty']

class CasesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cases
        fields=['case','answer']

class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tags
        fields=['tag_id']