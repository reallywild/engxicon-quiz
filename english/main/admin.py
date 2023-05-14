from django.contrib import admin
from .models import Dictionary, ProgDictionary, TVDictionary, BookDictionary

# Register your models here.
admin.site.register(Dictionary)
admin.site.register(ProgDictionary)
admin.site.register(TVDictionary)
admin.site.register(BookDictionary)