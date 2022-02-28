from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Topic, Lesson

# for testing
from django.http import HttpResponse


def home(request):
    return render(request, 'main/home.html')

def topics(request):
    all_topics = Topic.objects.all()
    context = {'topics': all_topics}
    return render(request, 'main/topics.html', context)

def lesson_example(request):
    return render(request, 'main/lesson_example.html')

def lessons(request, lesson_id):
    lesson = Lesson.objects.get(id=lesson_id)
    context = {'lesson': lesson}
    return render(request, 'main/lessons.html', context)