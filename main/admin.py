from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import Group,User
from.models import *

admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.register(Kutubxonachi)
admin.site.register(Kitob)
admin.site.register(Muallif)
admin.site.register(Record)
admin.site.register(Talaba)


