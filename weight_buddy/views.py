from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Training
from .models import ExercisesDetail
from .forms import TrainingForm
from .forms import ExercisesForm

# Create your views here.
def workout_list(request):
    trainings = Training.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'workout_buddy/workout_list.html', {'trainings': trainings})

def exercises_list(request):
    #exercises_list = get_object_or_404(ExercisesDetails)
    exercises = ExercisesDetail.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'exercises/exercises_list.html', {'exercises': exercises})

#def training_new(request):
#    form = TrainingForm()
#    return render(request, 'weight_buddy/training_edit.html', {'form': form})

def workout_detail(request, pk):
    training = get_object_or_404(Training, pk=pk)
    return render(request, 'workout_buddy/workout_detail.html', {'training': training})    

def training_new(request):
    if request.method == "POST":
        form = TrainingForm(request.POST)
        if form.is_valid():
            training = form.save(commit=False)
            training.author = request.user
            training.published_date = timezone.now()
            training.save()
            return redirect('workout_detail', pk=training.pk)
    else:
        form = TrainingForm()
    return render(request, 'workout_buddy/training_edit.html', {'form': form})

def exercises_new(request):
    if request.method == "POST":
        form = ExercisesForm(request.POST)
        if form.is_valid():
            exercises = form.save(commit=False)
            exercises.author = request.user
            exercises.published_date = timezone.now()
            exercises.save()
            return redirect('exercises_detail', pk=exercises.pk)
    else:
        form = ExercisesForm()
    return render(request, 'exercises/exercises_edit.html', {'form': form})

def training_edit(request, pk):
    training = get_object_or_404(Training, pk=pk)
    if request.method == "POST":
        form = TrainingForm(request.POST, instance=training)
        if form.is_valid():
            training = form.save(commit=False)
            training.author = request.user
            training.published_date = timezone.now()
            training.save()
            return redirect('workout_detail', pk=training.pk)
    else:
        form = TrainingForm(instance=training)
    return render(request, 'workout_buddy/training_edit.html', {'form': form})