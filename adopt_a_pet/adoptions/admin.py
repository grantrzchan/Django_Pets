from django.contrib import admin

from .models import Pet

#resgister class with decorator to tell admin which model it is associated with
# once created super user, use localhost:8000/admin to gain access

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ['name', 'species', 'breed', 'age', 'sex']