from django import forms

from .models import Training

class TrainingForm(forms.ModelForm):

    class Meta:
        model = Training
        fields = ('workout_name','workout_type', 'exercise','weight','exercise_one', 'weight_one', 
        'exercise_two','weight_two','exercise_tree', 'weight_tree', 'exercise_four', 
        'weight_four', 'exercise_five', 'weight_five')