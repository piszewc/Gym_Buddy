from django.shortcuts import render

# Create your views here.
def weight_list(request):
    return render(request, 'weight_buddy/weight_list.html', {})