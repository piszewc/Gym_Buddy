from django.contrib import admin
from .models import ExercisesDetail
from .models import Equipment
from .models import UserDetailsExercise
from .models import Training
from .models import WorkOut
from .models import Post

admin.site.register(ExercisesDetail)
admin.site.register(Equipment)
admin.site.register(UserDetailsExercise)
admin.site.register(Training)
admin.site.register(WorkOut)
admin.site.register(Post)
