from django.shortcuts import render
from django.utils import timezone
from .models import ExercisesList

def weight_list(request):
    exercises = ExercisesList.objects.filter(creation_date__lte=timezone.now()).order_by('creation_date')
    return render(request, 'exercises/exercise_list.html', {'exercises': exercises})