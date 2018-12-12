class ExerciseTypeListView(ListView):

    CHEST = 'CHEST'
    DELTS = 'DELTS'
    TRICEPS = 'TRICEPS'
    LEGS = 'LEGS'
    ABS = 'ABS'
    BACK = 'BACK'
    BICEPS = 'BICEPS'
    FOREARMS = 'FOREARMS'

    excercise_type_choices = ((CHEST, 'CHEST'),(DELTS, 'DELTS'),(TRICEPS, 'TRICEPS')
    ,(BACK, 'BACK'),(BICEPS, 'BICEPS'),(FOREARMS, 'FOREARMS')
    ,(LEGS, 'LEGS'),(ABS, 'ABS'),)

    workout_type = models.CharField(
        max_length=10,
        choices=excercise_type_choices,
        default=CHEST,
    )

	def __str__(self):
		return "%s %s" % (self.workout_type)	