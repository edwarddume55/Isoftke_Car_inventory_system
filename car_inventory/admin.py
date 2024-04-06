from django.contrib import admin
from .models import Car, Make, Model, Document, Expense

admin.site.register(Car)
admin.site.register(Make)
admin.site.register(Model)
admin.site.register(Document)
admin.site.register(Expense)