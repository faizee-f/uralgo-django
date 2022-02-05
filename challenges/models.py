from django.db import models
from accounts.models import Account
from ckeditor.fields import RichTextField

# Create your models here.

DIFFICULTY=[
    ('Easy','Easy'),
    ('Medium','Medium'),
    ('Hard','Hard'),
]

class Challenge(models.Model):
    created_by=models.ForeignKey(Account,on_delete=models.CASCADE)
    question=RichTextField()
    votes=models.IntegerField(default=0)
    difficulty=models.CharField(choices=DIFFICULTY,max_length=60)
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question

class Cases(models.Model):
    challenge_id=models.ForeignKey(Challenge, on_delete=models.CASCADE)
    case=models.CharField(max_length=255, blank=False)
    ans=models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.challenge_id


class TagList(models.Model):
    tag=models.CharField(max_length=50)

    def __str__(self):
        return self.tag

class Tags(models.Model):
    challenge_id=models.ForeignKey(Challenge, on_delete=models.CASCADE)
    tag_id=models.ForeignKey(TagList, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.challenge_id