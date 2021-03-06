from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from django.views.generic import ListView
from .models import Pacient
from .forms import PacientForm

class PacientsListView(ListView):
    model = Pacient

# Create your views here.
def get_pacient(request:HttpRequest):
    if request.method == "POST":
        form = PacientForm(request.POST)
        pacient = Pacient(name = form.data['name'], surname = form.data['surname'], cnp = form.data['cnp'],\
                          email = form.data['email'], phone = form.data['phone'])
        pacient.save()
        pass
        # name = form.data.name
    else:
        form = PacientForm()
    return render(request, 'scheduler/pacient.html', {'form':form})