from django.contrib import admin

from accounts.models import Account

# Register your models here.


class AccountAdmin(admin.ModelAdmin):
    fields = (
        "first_name",
        "last_name",
        "email",
        "password",
        "is_admin",
        "is_staff",
        "is_active",
        "is_verified",
    )
    readonly_fields = ("password",)


admin.site.register(Account, AccountAdmin)
