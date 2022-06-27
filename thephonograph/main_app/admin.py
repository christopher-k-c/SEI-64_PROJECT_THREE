from django.contrib import admin
from .models import Record, Tracklist, Artist
# Register your models here.


admin.site.register(Record),
admin.site.register(Tracklist),
admin.site.register(Artist),

