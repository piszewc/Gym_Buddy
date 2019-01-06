from django.db import models
from django.utils import timezone

class ExercisesDetail(models.Model):

	CARDIO = 'CARDIO'
	PLYO = "PLYO"
	WEIGHT = "WEIGHT"
	LAPS = "LAPS"

	excercise_type_choices = ((CARDIO,"CARDIO"), (PLYO, "PLYO"), (WEIGHT, "WEIGHT"), (LAPS,"LAPS"))
	
	excercise_type = models.CharField(
        max_length=10,
        choices=excercise_type_choices,
        default="WEIGHT",
    )

	excercise_name = models.CharField(max_length=100)
	excercise_description = models.CharField(max_length=1000,blank=True, null=True)
	
	created_date = models.DateTimeField(
            default=timezone.now)
	published_date = models.DateTimeField(
            blank=True, null=True)


	def publish(self):
		self.published_date = timezone.now()
		self.save()


	def __str__(self):
		return self.excercise_name	

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

	created_date = models.DateTimeField(
            default=timezone.now)
	published_date = models.DateTimeField(
            blank=True, null=True)


	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.workout_name