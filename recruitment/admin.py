from django.contrib import admin
from .models import Academics, UserProfile, Certifications, Experience

# Register your models here.

admin.site.register(Academics)
admin.site.register(Certifications)
admin.site.register(Experience)
admin.site.register(UserProfile)