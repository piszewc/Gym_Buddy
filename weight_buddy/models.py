from django.db import models
from django.utils import timezone

class Exercises(models.Model):

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

	excercise_name = models.CharField(max_length=100)
	set_repetitions_number = models.CharField(max_length=1000,blank=True, null=True)
	excercise_description = models.CharField(max_length=1000,blank=True, null=True)

	def __str__(self):
		return "%s %s" % (self.excercise_name, self.set_repetitions_number )	

DEFAULT_EXERCISE_ID = 1

class Training(models.Model):

	PUSH = 'PH'
	PULL = 'PL'
	LEG = 'LG'
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	workout_type_choices = ((PUSH, 'Push'),(PULL, 'Pull'),(LEG, 'Leg'),)
	workout_type = models.CharField(
        max_length=2,
        choices=workout_type_choices,
        default=PUSH,
    )
	
	workout_name =models.CharField(max_length=200)

	exercise = models.ForeignKey(Exercises, on_delete=models.SET_DEFAULT, default=DEFAULT_EXERCISE_ID, related_name='exercise')
	weight = models.SmallIntegerField(blank=True, null=True)

	exercise_one = models.ForeignKey(Exercises, on_delete=models.SET_DEFAULT, default=DEFAULT_EXERCISE_ID, related_name='exercise_one')
	weight_one = models.SmallIntegerField(blank=True, null=True)

	exercise_two = models.ForeignKey(Exercises, on_delete=models.SET_DEFAULT, default=DEFAULT_EXERCISE_ID, related_name='exercise_two')
	weight_two = models.SmallIntegerField(blank=True, null=True)

	exercise_tree = models.ForeignKey(Exercises, on_delete=models.SET_DEFAULT, default=DEFAULT_EXERCISE_ID, related_name='exercise_tree')
	weight_tree = models.SmallIntegerField(blank=True, null=True)

	exercise_four = models.ForeignKey(Exercises, on_delete=models.SET_DEFAULT, default=DEFAULT_EXERCISE_ID, related_name='exercise_four')
	weight_four = models.SmallIntegerField(blank=True, null=True)

	exercise_five = models.ForeignKey(Exercises, on_delete=models.SET_DEFAULT, default=DEFAULT_EXERCISE_ID, related_name='exercise_five')
	weight_five = models.SmallIntegerField(blank=True, null=True)

	created_date = models.DateTimeField(
            default=timezone.now)
	published_date = models.DateTimeField(
            blank=True, null=True)


	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.workout_name