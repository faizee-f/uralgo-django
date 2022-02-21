from django.db import models
from accounts.models import Account
from ckeditor.fields import RichTextField
# Create your models here.
from django.contrib.postgres.fields import ArrayField

try:
    from django.db.models import JSONField
except ImportError:
    from django.contrib.postgres.fields import JSONField


DIFFICULTY=[
    ('Easy','Easy'),
    ('Medium','Medium'),
    ('Hard','Hard'),
]

class Challenge(models.Model):
    created_by=models.ForeignKey(Account,on_delete=models.CASCADE)
    name=models.CharField(max_length=200,blank=True,null=True)
    question=RichTextField()
    report=models.IntegerField(default=0)
    likes=models.IntegerField(default=0)
    difficulty=models.CharField(choices=DIFFICULTY,max_length=60)
    modified_at=models.DateTimeField(auto_now=True)
    tags =ArrayField(models.CharField(max_length=200), blank=True)
    caseInput=JSONField()
    caseOutput=JSONField()
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def is_valid(self):
        if self.report<2:
            return True
        else:
            return False

class TagList(models.Model):
    tag=models.CharField(max_length=50)

    def __str__(self):
        return self.tag

    