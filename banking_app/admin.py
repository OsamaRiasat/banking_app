from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Account)
admin.site.register(Client)
admin.site.register(PhoneNumbers)
admin.site.register(Address)
admin.site.register(AccountOwner)
admin.site.register(Statement)
admin.site.register(Cosigner)
admin.site.register(Transaction)
admin.site.register(AccountHistory)
