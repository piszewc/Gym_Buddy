from django.shortcuts import render
from django.utils import timezone
from .models import Training

# Create your views here.
def weight_list(request):
    trainings = Training.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'weight_buddy/weight_list.html', {'trainings': trainings})