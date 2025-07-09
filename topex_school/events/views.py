from django.shortcuts import render, redirect
from .models import Event
from .forms import EventForm
from django.contrib.auth.decorators import login_required

def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

def event_detail(request, pk):
    event = Event.objects.get(pk=pk)
    return render(request, 'events/event_detail.html', {'event': event})

@login_required
def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('events:event_list')
    else:
        form = EventForm()
    return render(request, 'events/add_event.html', {'form': form})
