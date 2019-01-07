from django import forms

from .models import Training
from .models import ExercisesDetail

class TrainingForm(forms.ModelForm):

    class Meta:
        model = Training
        fields = ('workout_name',)


class ExercisesForm(forms.ModelForm):

    class Meta:
        model = ExercisesDetail
        fields = ('excercise_name','excercise_type','excercise_description','excercise_major_muscule','excercise_major_muscule')