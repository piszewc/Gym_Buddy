from django.contrib import admin
from .models import Training
from .models import ExercisesDetail
from .models import Equipment


admin.site.register(Training)
admin.site.register(ExercisesDetail)
admin.site.register(Equipment)

