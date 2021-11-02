from django.contrib import admin
from .models import *

class StatistDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'save_books', 'save_date', 'save_books_name')

admin.site.register(Autor)
admin.site.register(Books)
admin.site.register(Review)
admin.site.register(Shop)
admin.site.register(StatistData, StatistDataAdmin)

