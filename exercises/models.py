from django.db import models

# Create your models here.
class ExercisesList(models.Model):
    exercise_name
    equipment
    exercise_type
    major_muscle
    minor_muscle
    description
    example
    notes
    modifications
