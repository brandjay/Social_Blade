from pydoc_data import topics
from django.contrib import admin
from post.models import Topic, Entry

# Register your models here.

admin.site.register(Topic)
admin.site.register(Entry)

