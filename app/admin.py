from multiprocessing.connection import Client
from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Cliente)
admin.site.register(Region)
admin.site.register(Comuna)
admin.site.register(Provincia)