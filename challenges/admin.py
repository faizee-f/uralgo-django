from django.contrib import admin

from challenges.models import Challenge,TagList

# Register your models here.
admin.site.register(Challenge)
admin.site.register(TagList)