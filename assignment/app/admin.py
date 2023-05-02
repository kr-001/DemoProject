from django.contrib import admin
from .models import Artist, Work

# Register your models here.
from .models import Client
admin.site.register(Client)
admin.site.register(Artist)
admin.site.register(Work)
