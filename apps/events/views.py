from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Event

def event_list(request):
    return HttpResponse("I am events")

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return HttpResponse(f"I am event detail for: {event.title}")

def upcoming_events(request):
    return HttpResponse("I am upcoming events")