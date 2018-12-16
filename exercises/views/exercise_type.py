from django.db import models

class ExerciseTypeListView(models.Model):

    CARDIO = 'CR'
    PLYO = 'PL'
    WEIGHT = 'WG'
    LAPS = 'LP'

    excercise_type_choices = ((CARDIO, 'CARDIO'),(PLYO, 'PLYO'),(WEIGHT, 'WEIGHT')
    ,(LAPS, 'LAPS'),)

    excercise_type = models.CharField(
        max_length=2,
        choices=excercise_type_choices,
        default=CARDIO,
    )
    
    excercise_type_description = models.CharField(max_length=1000)

    def __str__(self):
        return "%s" % (self.excercise_type)