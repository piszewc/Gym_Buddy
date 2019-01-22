from django import forms

from .models import ExercisesDetail
from .models import Equipment
from .models import UserDetailsExercise

class ExercisesForm(forms.ModelForm):

    class Meta:
        model = ExercisesDetail
        fields = ('name','type','major_muscule','minior_muscule','example','description','modification','equipment')

class Equipment(forms.ModelForm):

    class Meta:
        model = Equipment
        fields = ('name','description','image')

class UserDetailsExercise(forms.Form):

    class Meta:
        model = UserDetailsExercise
        fields = ('exercise','sets','repets','rest','notes')