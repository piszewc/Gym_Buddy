from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Training
from .forms import TrainingForm

# Create your views here.
def weight_list(request):
    trainings = Training.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'weight_buddy/weight_list.html', {'trainings': trainings})

#def training_new(request):
#    form = TrainingForm()
#    return render(request, 'weight_buddy/training_edit.html', {'form': form})

def weight_detail(request, pk):
    training = get_object_or_404(Training, pk=pk)
    return render(request, 'weight_buddy/weight_detail.html', {'training': training})    

def training_new(request):
    if request.method == "POST":
        form = TrainingForm(request.POST)
        if form.is_valid():
            training = form.save(commit=False)
            training.author = request.user
            training.published_date = timezone.now()
            training.save()
            return redirect('weight_detail', pk=training.pk)
    else:
        form = TrainingForm()
    return render(request, 'weight_buddy/training_edit.html', {'form': form})

def training_edit(request, pk):
    training = get_object_or_404(Training, pk=pk)
    if request.method == "POST":
        form = TrainingForm(request.POST, instance=training)
        if form.is_valid():
            training = form.save(commit=False)
            training.author = request.user
            training.published_date = timezone.now()
            training.save()
            return redirect('weight_detail', pk=training.pk)
    else:
        form = TrainingForm(instance=training)
    return render(request, 'weight_buddy/training_edit.html', {'form': form})