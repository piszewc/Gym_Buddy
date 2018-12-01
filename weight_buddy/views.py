from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Training
from .forms import TrainingForm

# Create your views here.
def weight_list(request):
    trainings = Training.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'weight_buddy/weight_list.html', {'trainings': trainings})

def training_new(request):
    form = TrainingForm()
    return render(request, 'weight_buddy/training_edit.html', {'form': form})

def weight_detail(request, pk):
    training = get_object_or_404(Training, pk=pk)
    return render(request, 'weight_buddy/weight_detail.html', {'training': training})    