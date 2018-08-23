from django.contrib import admin
from .models import Track, TrackCourse
# Register your models here.

@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ("host", "time", "ip")

@admin.register(TrackCourse)
class TrackCourseAdmin(admin.ModelAdmin):
    list_display = ("course_id", "user_id")    
