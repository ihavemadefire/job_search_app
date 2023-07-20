from django.contrib import admin
from .models import *

admin.site.register(PersonOfContact)
admin.site.register(Company)
admin.site.register(Application)
admin.site.register(ContactEvent)
admin.site.register(Blog)