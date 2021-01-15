from django.shortcuts import render
from events.models import Event
from datetime import date

def events(request):

    all_events = Event.objects.all()
    upcomming_events = Event.objects.filter(date__gte=date.today())
    past_events = Event.objects.filter(date__lt=date.today())

    context = {
        'all_events': all_events,
        'upcomming_events': upcomming_events,
        'past_events': past_events
    }

    return render(request, 'events.html', context=context)
