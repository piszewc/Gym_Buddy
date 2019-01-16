from django.db import models
from django.utils import timezone

class Equipment(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=1000,blank=True, null=True)
	image = models.ImageField(upload_to='equipment_images/', blank=True, null=True)

	def __str__(self):
		return self.name


class ExercisesDetail(models.Model):

	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

	CARDIO = 'CARDIO'
	PLYO = "PLYO"
	WEIGHT = "WEIGHT"
	LAPS = "LAPS"

	type_choices = ((CARDIO,"CARDIO"), (PLYO, "PLYO"), (WEIGHT, "WEIGHT"), (LAPS,"LAPS"))
	
	type = models.CharField(
        max_length=10,
        choices=type_choices,
        default="WEIGHT",
    )
    
	FULL_BODY = 'FULL_BODY'
	BACK = 'BACK'
	CORE = 'CORE'
	ARMS = 'ARMS'
	LEGS = 'LEGS'

	major_muscule_choices = ((FULL_BODY,"FULL BODY"), (BACK, "BACK"), (CORE, "CORE"), (ARMS,"ARMS"), (LEGS,'LEGS'))

	major_muscule = models.CharField(
        max_length=10,
        choices=major_muscule_choices,
        default="FULL BODY",
    )

	BICEP = 'BICEP'
	CALVES = 'CALVES'
	CHEST = 'CHEST'
	GLUTES = 'GLUTES'
	HAMSTRINGS = 'HAMSTRINGS'
	INNER_THIGH = 'INNER_THIGH'
	LATS = 'LATS'
	OBLIQUE = 'OBLIQUE'
	OUTER_THIGH = 'OUTER_THIGH'
	QUADS = 'QUADS'
	SHOULDERS = 'SHOULDERS'
	TRICEP = 'TRICEP'

	minior_muscule_choices = ((BICEP,"BICEP"), (CALVES, "CALVES"), (CHEST, "CHEST"), (GLUTES,"GLUTES"), (HAMSTRINGS,'HAMSTRINGS'), (INNER_THIGH,'INNER THIGH'), 
	(LATS,'LATS'), (OBLIQUE,'OBLIQUE'), (OUTER_THIGH,'OUTER THIGH'), (QUADS,'QUADS'), (SHOULDERS,'SHOULDERS'), (TRICEP,'TRICEP'))

	minior_muscule = models.CharField(
        max_length=10,
        choices=minior_muscule_choices,
        default="BICEP",
    )


	name = models.CharField(max_length=100)
	description = models.CharField(max_length=1000,blank=True, null=True)
	modification = models.CharField(max_length=1000,blank=True, null=True)

	example = models.ImageField(upload_to='exercise_video/', blank=True, null=True)

	created_date = models.DateTimeField(
            default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	equipment = models.ManyToManyField(Equipment)


	def publish(self):
		self.published_date = timezone.now()
		self.save()


	def __str__(self):
		return self.name	


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