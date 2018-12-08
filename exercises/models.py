from django.db import models

# Create your models here.
class ExercisesList(models.Model):


class Equipment(models.Model):
     '''
    Equipment used or needed by an exercise
    '''

    name = models.CharField(max_length=50,
                            verbose_name=_('Name'))

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

