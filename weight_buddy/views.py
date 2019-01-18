import csv,io
from django.contrib import messages
from django.contrib.auth.decorators import permission_required

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Training
from .models import ExercisesDetail
from .forms import TrainingForm
from .forms import ExercisesForm



# Create your views here.
def home_page(request):
    return render(request, 'workout_buddy/home_page.html',)

def contact_page(request):
    return render(request, 'workout_buddy/contact_page.html',)

def workout_list(request):
    training = Training.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'workout_buddy/workout_list.html', {'training': training})


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


@permission_required('admin.can_add_log_entry')
def exercises_upload(request):
    template = "workout_buddy/exercises_upload.html"

    prompt = {
        'order': 'Order of CSV should be name, type, major_muscule, minior_muscule, description, modification'
    }

    if request.method == 'GET':
        return render(request, template, prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not CSV file')

    data_set = csv_file.read().decode('utf-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar='"'):
        _, created = ExercisesDetail.objects.update_or_create(
        author = request.user,
        name = column[1],
        type = column[2],
        major_muscule = column[3],
        minior_muscule = column[4],
        example = column[5],
        description = column[6],
        modification = column[7],
        published_date = "2019-01-17 22:31:44.781964" 
        )
    context = {}
    return render(request, template, context)
