class ExerciseTypeListView(ListView, models.Model):

    CARDIO = 'CR'
    PLYO = 'PL'
    WEIGHT = 'WG'
    LAPS = 'LP'

    excercise_type_choices = ((CARDIO, 'CARDIO'),(PLYO, 'PLYO'),(WEIGHT, 'WEIGHT')
    ,(LAPS, 'LAPS'),)

    workout_type = models.CharField(
        max_length=2,
        choices=excercise_type_choices,
        default=CARDIO,
    )

    def __str__(self):
        return "%s" % (self.workout_type)	