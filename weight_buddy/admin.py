from django.contrib import admin
from .models import Training
from .models import Exercise

admin.site.register(Training)
admin.site.register(Exercise)