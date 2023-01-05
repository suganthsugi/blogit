from django.contrib import admin

from .models import *

# Register your models here.


admin.site.register(Blog)
admin.site.register(UserTag)
admin.site.register(Blogger)
admin.site.register(SupervisorReqs)