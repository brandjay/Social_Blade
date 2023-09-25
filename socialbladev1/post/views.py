from django.shortcuts import render
from .models import Topic, Entry

def topic_list(request):
    topics = Topic.objects.all()
    entries = Entry.objects.all()
    context = {
        'topics': topics,
        'entries': entries,
    }
    return render(request, 'post/topic_list.html', context)
