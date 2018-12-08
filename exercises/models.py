from django.db import models

# Create your models here.
class ExercisesList(models.Model):

    '''
    Model for an exercise
    '''

    objects = SubmissionManager()
    '''Custom manager'''

    category = models.ForeignKey(ExerciseCategory,
                                 verbose_name=_('Category'))
    description = models.TextField(max_length=2000,
                                   verbose_name=_('Description'),
                                   validators=[MinLengthValidator(40)])
    '''Description on how to perform the exercise'''

    name = models.CharField(max_length=200,
                            verbose_name=_('Name'))
    '''The exercise's name, with correct upercase'''

    name_original = models.CharField(max_length=200,
                                     verbose_name=_('Name'),
                                     default='')
    '''The exercise's name, as entered by the user'''

    major_muscle = models.ManyToManyField(MajorMuscle,
                                     blank=True,
                                     verbose_name=_('Major Muscle'))
    '''Main muscles trained by the exercise'''

    minor_muscle = models.ManyToManyField(MinorMuscle,
                                               verbose_name=_('Minor Muscle'),
                                               related_name='minor_muscle',
                                               blank=True)
    '''Secondary muscles trained by the exercise'''

    equipment = models.ManyToManyField(Equipment,
                                       verbose_name=_('Equipment'),
                                       blank=True)
    '''Equipment needed by this exercise'''

    creation_date = models.DateField(_('Date'),
                                     auto_now_add=True,
                                     null=True,
                                     blank=True)
    '''The submission date'''


    uuid = models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='UUID')

    '''
    Globally unique ID, to identify the exercise across installations
    '''

    #
    # Django methods
    #
    class Meta:
        ordering = ["name", ]

    def get_absolute_url(self):
        '''
        Returns the canonical URL to view an exercise
        '''
        return reverse('exercise:exercise:view', kwargs={'id': self.id, 'slug': slugify(self.name)})

    def save(self, *args, **kwargs):
        '''
        Reset all cached infos
        '''
        self.name = smart_capitalize(self.name_original)
        super(Exercise, self).save(*args, **kwargs)

        # Cached objects
        cache.delete(cache_mapper.get_exercise_muscle_bg_key(self))

        # Cached template fragments
        for language in Language.objects.all():
            delete_template_fragment_cache('muscle-overview', language.id)
            delete_template_fragment_cache('exercise-overview', language.id)
            delete_template_fragment_cache('exercise-overview-mobile', language.id)
            delete_template_fragment_cache('equipment-overview', language.id)

        # Cached workouts
        for set in self.set_set.all():
            reset_workout_canonical_form(set.exerciseday.training_id)

    def delete(self, *args, **kwargs):
        '''
        Reset all cached infos
        '''

        # Cached objects
        cache.delete(cache_mapper.get_exercise_muscle_bg_key(self))

        # Cached template fragments
        for language in Language.objects.all():
            delete_template_fragment_cache('muscle-overview', language.id)
            delete_template_fragment_cache('exercise-overview', language.id)
            delete_template_fragment_cache('exercise-overview-mobile', language.id)
            delete_template_fragment_cache('equipment-overview', language.id)

        # Cached workouts
        for set in self.set_set.all():
            reset_workout_canonical_form(set.exerciseday.training.pk)

        super(Exercise, self).delete(*args, **kwargs)

    def __str__(self):
        '''
        Return a more human-readable representation
        '''
        return self.name


class Equipment(models.Model):
        '''
    Equipment used or needed by an exercise
    '''
    name = models.CharField(max_length=50, verbose_name=_('Name'))

    class Meta:
        '''
        Set default ordering
        '''
        ordering = ["name", ]

    def __str__(self):
        '''
        Return a more human-readable representation
        '''
        return self.name

    def get_owner_object(self):
        '''
        Equipment has no owner information
        '''
        return False

class MajorMuscle(models.Model):

   name = models.CharField(max_length=50,
                            verbose_name=_('Name'),
                            help_text=_('Major Muscle'))

    # Whether to use the front or the back image for background
    is_front = models.BooleanField(default=1)

    # Metaclass to set some other properties
    class Meta:
        ordering = ["name", ]

    def __str__(self):
        '''
        Return a more human-readable representation
        '''
        return self.name

    def get_owner_object(self):
        '''
        Muscle has no owner information
        '''
        return False

class MinorMuscle(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name=_('Name'),
                            help_text=_('Minor Muscle'))

    # Whether to use the front or the back image for background
    is_front = models.BooleanField(default=1)

    # Metaclass to set some other properties
    class Meta:
        ordering = ["name", ]

    def __str__(self):
        '''
        Return a more human-readable representation
        '''
        return self.name

    def get_owner_object(self):
        '''
        Muscle has no owner information
        '''
        return False

class ExerciseType(models.Model):
    name = models.CharField(max_length=50,
                        verbose_name=_('Name'),
                        help_text=_('Exercise Type'))

    # Whether to use the front or the back image for background
    is_front = models.BooleanField(default=1)

    # Metaclass to set some other properties
    class Meta:
        ordering = ["name", ]

    def __str__(self):
        '''
        Return a more human-readable representation
        '''
        return self.name

    def get_owner_object(self):
        '''
        Muscle has no owner information
        '''
        return False

