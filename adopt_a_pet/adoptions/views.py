from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import Pet


def home(request):
    pets = Pet.objects.all()
    #use render() to render HTML
    return render(request, 'home.html', {'pets': pets})

def pet_detail(request, id):
    #create try/except to catch any id that may be passed for ehich no pets are assigned
    try:
        pet = Pet.objects.get(id=id)
    except Pet.DoesNotExist:
        #raise 404 if pet is not found
        raise Http404('Pet not found')
    return render(request, 'pet_detail.html', {'pet': pet})

