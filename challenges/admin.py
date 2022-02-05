from django.contrib import admin

from challenges.models import Cases, Challenge, Tags,TagList

# Register your models here.
admin.site.register(Challenge)
admin.site.register(Cases)
admin.site.register(TagList)
admin.site.register(Tags)