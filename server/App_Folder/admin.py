from django.contrib import admin
from .models import Papers, Keywords, Profile, Reads

# Register your models here.
admin.site.register(Papers)
admin.site.register(Keywords)
admin.site.register(Profile)
admin.site.register(Reads)



