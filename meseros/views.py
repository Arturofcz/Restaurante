from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy


from meseros.forms import MeseroForm
from meseros.models import Mesero

from django.views.generic import ListView, DeleteView, CreateView, UpdateView


# Create your views here.

def meseros_list(request):

    """Obtener todos los elementos de una tabla en la bd"""
    meseros = Mesero.objects.all()

    query = Q(pais__startswith='Per') & Q(edad__lt=30)
    meseros = Mesero.objects.filter(query)

    return render(request, 'meseros_list.html', context={'data': meseros})



def meseros_details(request):
    """Obtener todos los elementos de una tabla en la BD"""
    meseros = Mesero.objects.all()



    return render(request, 'meseros_details.html', context={'data': meseros})




def mesero_create(request):
    # request.method = "POST"
    if request.method == "POST":
        print("ES UN POST")
        form = MeseroForm(request.POST)
        if form.is_valid():
            # nombre = form.cleaned_data['nombre']
            # print("Nombre: {}".format(nombre))
            # edad = form.cleaned_data['edad']
            # pais = form.cleaned_data['pais']
            try:
                form.save()
                return redirect('meseros_list')
            except:
                pass
    else:
        form = MeseroForm
    return render(request, 'mesero-create.html', {'form': form})

class MeserosList(ListView):
    #permission_classes = [IsAuthenticated]
    model = Mesero
    template_name = 'meseros_vc.html'

class MeserosCreate(CreateView):
    model = Mesero
    form_class = MeseroForm
    template_name = 'mesero-create.html'
    success_url = reverse_lazy('meseros_list_vc')

class MeseroUpdate(UpdateView):
    model = Mesero
    form_class = MeseroForm
    template_name = 'mesero-update-vc.html'
    success_url = reverse_lazy('meseros_list_vc')


class MeseroDelete(DeleteView):
    model = Mesero
    success_url = reverse_lazy('meseros_list_vc')
    template_name = 'mesero-confirm-delete.html'

