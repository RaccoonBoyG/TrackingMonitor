from django.shortcuts import render
import json
from django.shortcuts import render, redirect
from .models import \
    Track, TrackCourse

def upload_from_json(request):
    if request.method == 'POST':
        track = json.loads(request.POST.get("json_value", None))

        return render(request, 'roo/upload_from_json.html')