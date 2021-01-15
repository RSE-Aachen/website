from django.shortcuts import render
from events.models import Event
from datetime import date

def events(request):

    local_events = Event.objects.filter(is_local=True)
    nonlocal_events = Event.objects.filter(is_local=False)
    local_upcomming_events = local_events.filter(date__gte=date.today())
    nonlocal_upcomming_events = nonlocal_events.filter(date__gte=date.today())

    context = {
        'local_upcomming_events': local_upcomming_events,
        'non_local_upcomming_events': nonlocal_upcomming_events,
    }

    return render(request, 'events.html', context=context)
