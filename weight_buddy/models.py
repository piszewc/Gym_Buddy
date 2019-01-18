from django.db import models
from django.utils import timezone
from multiselectfield import MultiSelectField

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
	MACHINE = "MACHINE"


	type_choices = ((CARDIO,"CARDIO"), (PLYO, "PLYO"), (WEIGHT, "WEIGHT"), (LAPS,"LAPS"), (MACHINE,"MACHINE"))
	
	type = MultiSelectField(
        max_length=20,
        choices=type_choices,
        default="WEIGHT",
    )
    
	FB = 'FULL_BODY'
	BK = 'BACK'
	CR = 'CORE'
	AR = 'ARMS'
	LG = 'LEGS'

	major_muscule_choices = ((FB,"FULL BODY"), (BK, "BACK"), (CR, "CORE"), (AR,"ARMS"), (LG,'LEGS'))

	major_muscule = MultiSelectField(
        max_length=19,
        choices=major_muscule_choices,
        default=FB,
    )

	BC = 'BICEP'
	CL = 'CALVES'
	CH = 'CHEST'
	GT = 'GLUTES'
	HS = 'HAMSTRINGS'
	IT = 'INNER_THIGH'
	LT = 'LATS'
	OQ = 'OBLIQUE'
	OT = 'OUTER_THIGH'
	QD = 'QUADS'
	SD = 'SHOULDERS'
	TC = 'TRICEP'

	minior_muscule_choices = ((BC,"BICEP"), (CL, "CALVES"), (CH, "CHEST"), (GT,"GLUTES"), (HS,'HAMSTRINGS'), (IT,'INNER THIGH'), 
	(LT,'LATS'), (OQ,'OBLIQUE'), (OT,'OUTER THIGH'), (QD,'QUADS'), (SD,'SHOULDERS'), (TC,'TRICEP'))

	minior_muscule = MultiSelectField(
        max_length=50,
        choices=minior_muscule_choices,
        default=BC,
    )


	name = models.CharField(max_length=100)
	description = models.CharField(max_length=1000,blank=True, null=True)
	modification = models.CharField(max_length=1000,blank=True, null=True)

	example = models.ImageField(upload_to='exercise_video/', blank=True, null=True)

	created_date = models.DateTimeField(
            default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	equipment = models.ManyToManyField('Equipment')

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