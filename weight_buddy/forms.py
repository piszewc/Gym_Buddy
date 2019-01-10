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
        fields = ('name','type','major_muscule','minior_muscule','example','description','modification',)
       