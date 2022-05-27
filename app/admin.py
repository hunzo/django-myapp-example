from django.contrib import admin
from .models import RecipientList, EmailGroupList, EmailList
# Register your models here.

admin.site.register(RecipientList)
admin.site.register(EmailList)
admin.site.register(EmailGroupList)
