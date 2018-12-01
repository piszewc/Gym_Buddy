from django.db import models
from django.utils import timezone

class Exercises(models.Model):

	excercise_name = models.CharField(max_length=100)
	excercise_description = models.CharField(max_length=1000,blank=True, null=True)

	def __str__(self):
		return "%s %s" % (self.excercise_name, self.excercise_description)	

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

	exercise = models.ForeignKey(Exercises, on_delete=models.CASCADE, default=DEFAULT_EXERCISE_ID)

	weight = models.SmallIntegerField()
	created_date = models.DateTimeField(
            default=timezone.now)
	published_date = models.DateTimeField(
            blank=True, null=True)


	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.exercise