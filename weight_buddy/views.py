import csv
import io
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.core.mail import send_mail
from django.conf import settings

from django.template.loader import render_to_string

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import ExercisesDetail
from .forms import ExercisesForm

from .models import Post
from .forms import PostForm

# Create your views here.


def home_page(request):
    return render(request, 'workout_buddy/home_page.html', {'nbar': 'home_page'})


def about_page(request):
    return render(request, 'workout_buddy/about_page.html', {'nbar': 'about_page'})


def exercise_list(request):
    exercises = ExercisesDetail.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'exercises/exercise_list.html', {'exercises': exercises, 'nbar': 'exercise_list'})


def exercise_detail(request, pk, slug):
    exercise = get_object_or_404(ExercisesDetail, pk=pk, slug=slug)
    return render(request, 'exercises/exercise_detail.html', {'exercise': exercise})


def exercise_new(request):
    if request.method == "POST":
        form = ExercisesForm(request.POST, request.FILES)
        if form.is_valid():
            exercise = form.save(commit=False)
            exercise.author = request.user
            exercise.published_date = timezone.now()
            exercise.save()
            return redirect('exercise_detail', pk=exercise.pk, slug=exercise.slug)
    else:
        form = ExercisesForm()
    return render(request, 'exercises/exercise_edit.html', {'form': form})


def exercise_edit(request, pk, slug):
    exercise = get_object_or_404(ExercisesDetail, pk=pk, slug=slug)
    if request.method == "POST":
        form = ExercisesForm(request.POST, request.FILES, instance=exercise)
        if form.is_valid():
            exercise = form.save(commit=False)
            exercise.author = request.user
            exercise.published_date = timezone.now()
            exercise.save()
            return redirect('exercise_detail', pk=exercise.pk, slug=exercise.slug)
    else:
        form = ExercisesForm(instance=exercise)
    return render(request, 'exercises/exercise_edit.html', {'form': form})


@permission_required('admin.can_add_log_entry')
def exercises_upload(request):
    template = "workout_buddy/exercises_upload.html"

    prompt = {
        'order': 'Order of CSV should be name, type, major_muscule, minior_muscule, execution, comments'
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
            author=request.user,
            name=column[1],
            type=column[2],
            major_muscule=column[3],
            minior_muscule=column[4],
            example=column[5],
            execution=column[6],
            comments=column[7],
            example_thumbnail=column[9],
            published_date="2019-01-17 22:31:44.781964"
        )
    context = {}
    return render(request, template, context)


def contact_page(request):
    if request.method == 'POST':
        message = request.POST['message']
        name = request.POST['name']
        subject = request.POST['subject']
        email = request.POST['email']
        context = {'name': name, 'subject': subject,
                   'email': email,  'message': message}
        template = render_to_string(
            'workout_buddy/email_template.html', context)
        send_mail('Contact Form', template, settings.EMAIL_HOST_USER,
                  ['pszewc@zoho.eu'], fail_silently=False)

    return render(request, 'workout_buddy/contact_page.html', {'nbar': 'contact_page'})


def post_list(request):
    posts = Post.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk, slug):
    post = get_object_or_404(Post, pk=pk, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk, slug=post.slug)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk, slug):
    post = get_object_or_404(Post, pk=pk, slug=slug)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk, slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
