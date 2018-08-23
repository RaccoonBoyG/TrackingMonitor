from django.shortcuts import render
import json
from django.shortcuts import render, redirect
from .models import \
    Track, TrackCourse

def upload_from_json(request):
        #track = json.loads(request.POST.get("json_value", None))
        return render(request, 'upload_from_json.html')