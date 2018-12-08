from django.shortcuts import render

def weight_list(request):
    exercises = ExercisesList.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'exercises/exercise_list.html', {'exercises': exercises})