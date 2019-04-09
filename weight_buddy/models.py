from django.db import models
from django.utils import timezone
from multiselectfield import MultiSelectField
from django.conf import settings


class Equipment(models.Model):
	name = models.CharField(max_length=100)
	execution = models.CharField(max_length=1000, blank=True, null=True)
	image = models.ImageField(
		upload_to='equipment_images/', blank=True, null=True)

	def __str__(self):
		return self.name


class ExercisesDetail(models.Model):

	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

	CARDIO = 'CARDIO'
	PLYO = "PLYO"
	WEIGHT = "WEIGHT"
	LAPS = "LAPS"
	MACHINE = "MACHINE"

	type_choices = ((CARDIO, "CARDIO"), (PLYO, "PLYO"),
	                (WEIGHT, "WEIGHT"), (LAPS, "LAPS"), (MACHINE, "MACHINE"))

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

	major_muscule_choices = ((FB, "FULL BODY"), (BK, "BACK"),
	                         (CR, "CORE"), (AR, "ARMS"), (LG, 'LEGS'))

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

	minior_muscule_choices = ((BC, "BICEP"), (CL, "CALVES"), (CH, "CHEST"), (GT, "GLUTES"), (HS, 'HAMSTRINGS'), (IT, 'INNER THIGH'),
                           (LT, 'LATS'), (OQ, 'OBLIQUE'), (OT, 'OUTER THIGH'), (QD, 'QUADS'), (SD, 'SHOULDERS'), (TC, 'TRICEP'))

	minior_muscule = MultiSelectField(
            max_length=50,
            choices=minior_muscule_choices,
            default=BC,
        )

	name = models.CharField(max_length=100)
	execution = models.CharField(max_length=1000, blank=True, null=True)
	comments = models.CharField(max_length=1000, blank=True, null=True)
	preparation = models.CharField(max_length=1000, blank=True, null=True) 

	example = models.ImageField(
		upload_to='exercise_video/', blank=True, null=True)
	example_thumbnail = models.ImageField(
		upload_to='exercise_video/thumbnail/', blank=True, null=True)

	created_date = models.DateTimeField(
            default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	equipment = models.ManyToManyField('Equipment')

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.name


class UserDetailsExercise(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	exercises_detail = models.ForeignKey(
		ExercisesDetail, on_delete=models.CASCADE)
	sets = models.CharField(max_length=200, blank=True, null=True)
	repets = models.CharField(max_length=200, blank=True, null=True)
	rest = models.CharField(max_length=200, blank=True, null=True)
	notes = models.CharField(max_length=200, blank=True, null=True)
	name = models.CharField(max_length=200, blank=True, null=True)

	created_date = models.DateTimeField(
		default=timezone.now)

	def create(self):
		self.created_date = timezone.now()
		self.save()

	def __str__(self):
		return self.name


class Training(models.Model):

	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	user_details_exercises = models.ManyToManyField('UserDetailsExercise')

	name = models.CharField(max_length=200, blank=True, null=True)

	minior_muscule_used = models.CharField(max_length=200, blank=True, null=True)
	comments = models.CharField(max_length=200, blank=True, null=True)

	created_date = models.DateTimeField(
            default=timezone.now)

	def create(self):
		self.created_date = timezone.now()
		self.save()

	def __str__(self):
		return self.name


class WorkOut(models.Model):

	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	training = models.ManyToManyField('Training')

	name = models.CharField(max_length=200, blank=True, null=True)

	notes = models.CharField(max_length=200, blank=True, null=True)
	created_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
			return self.name


class Post(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	text = models.TextField()
	image = models.ImageField(
		upload_to='post_images/', blank=True, null=True)
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title
