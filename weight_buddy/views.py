from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Training
from .models import ExercisesDetail
from .forms import TrainingForm
from .forms import ExercisesForm

# Create your views here.
def workout_list(request):
    training = Training.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'workout_buddy/workout_list.html', {'training': training})

def home_page(request):
    return render(request, 'workout_buddy/home_page.html',)


def exercise_list(request):
    exercises = ExercisesDetail.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'exercises/exercise_list.html', {'exercises': exercises})

#def training_new(request):
#    form = TrainingForm()
#    return render(request, 'weight_buddy/training_edit.html', {'form': form})

def workout_detail(request, pk):
    training = get_object_or_404(Training, pk=pk)
    return render(request, 'workout_buddy/workout_detail.html', {'training': training})    

def exercise_detail(request, pk):
    exercise = get_object_or_404(ExercisesDetail, pk=pk)
    return render(request, 'exercises/exercise_detail.html', {'exercise': exercise})    


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

def exercise_new(request):
    if request.method == "POST":
        form = ExercisesForm(request.POST)
        if form.is_valid():
            exercise = form.save(commit=False)
            exercise.author = request.user
            exercise.published_date = timezone.now()
            exercise.save()
            return redirect('exercise_detail', pk=exercise.pk)
    else:
        form = ExercisesForm()
    return render(request, 'exercises/exercise_edit.html', {'form': form})

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

    
def exercise_edit(request, pk):
    exercise = get_object_or_404(ExercisesDetail, pk=pk)
    if request.method == "POST":
        form = ExercisesForm(request.POST, instance=exercise)
        if form.is_valid():
            exercise = form.save(commit=False)
            exercise.author = request.user
            exercise.published_date = timezone.now()
            exercise.save()
            return redirect('exercise_detail', pk=exercise.pk)
    else:
        form = ExercisesForm(instance=exercise)
    return render(request, 'exercises/exercise_edit.html', {'form': form})