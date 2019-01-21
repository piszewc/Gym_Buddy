from django import forms

from .models import ExercisesDetail
from .models import Equipment
from .models import UserDetailsExercises

class ExercisesForm(forms.ModelForm):

    class Meta:
        model = ExercisesDetail
        fields = ('name','type','major_muscule','minior_muscule','example','description','modification','equipment')

class Equipment(forms.ModelForm):

    class Meta:
        model = Equipment
        fields = ('name','description','image')

class UserDetailsExercises(forms.ModelForm):

    class Meta:
        model = UserDetailsExercises
        fields = ('exercises_detail','sets','repets','rest','notes')