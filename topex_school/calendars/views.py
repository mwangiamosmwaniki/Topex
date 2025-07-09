from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import CalendarEvent
from .forms import CalendarEventForm
from datetime import date

def calendar_home(request):
    events = CalendarEvent.objects.order_by('start_date')
    return render(request, 'calendars/calendar_home.html', {'events': events})

@login_required
@user_passes_test(lambda u: u.profile.role in ['admin', 'lecturer'])
def add_event(request):
    if request.method == 'POST':
        form = CalendarEventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.created_by = request.user
            event.save()
            return redirect('calendar_home')
    else:
        form = CalendarEventForm()
    return render(request, 'calendars/add_event.html', {'form': form})
