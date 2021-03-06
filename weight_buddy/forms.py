from django import forms

from .models import ExercisesDetail
from .models import Equipment
from .models import UserDetailsExercise
from .models import Training
from .models import WorkOut
from .models import Post

class ExercisesForm(forms.ModelForm):

    class Meta:
        model = ExercisesDetail
        fields = ('name','type','major_muscule','minior_muscule','example','execution','comments','equipment','example_thumbnail', 'preparation')

class EquipmentForm(forms.ModelForm):

    class Meta:
        model = Equipment
        fields = ('name','execution','image')

class UserDetailsExerciseForm(forms.Form):

    class Meta:
        model = UserDetailsExercise
        fields = ('exercise','sets','repets','rest','notes')


class TrainingForm(forms.Form):

    class Meta:
        model = Training
        fields = ('user_details_exercises','name','minior_muscule_used','comments')

class WorkoutForm(forms.Form):

    class Meta:
        model = WorkOut
        fields = ('training','name','notes')

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'image')
