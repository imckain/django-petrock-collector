from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from .models import Petrock, Hat

# Create your views here.
def home(request): 
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def petrocks_index(request):
    petrocks = Petrock.objects.all()
    return render(request, 'petrocks/index.html', { 'petrocks': petrocks })

def petrocks_detail(request, petrock_id):
    petrock = Petrock.objects.get(id=petrock_id)
    return render(request, 'petrocks/detail.html', { 'petrock': petrock })

class PetrockCreate(CreateView):
    model = Petrock
    fields = '__all__'

class PetrockUpdate(UpdateView):
    model = Petrock
    fields = ['rockType', 'description', 'personality']

class PetrockDelete(DeleteView):
    model = Petrock
    success_url = '/petrocks/'

class HatList(ListView):
    model = Hat

class HatDetailView(DetailView):
    model = Hat

class HatCreateView(CreateView):
    model = Hat
    fields = '__all__'

class HatUpdateView(UpdateView):
    model = Hat
    fields = '__all__'

class HatDeleteView(DeleteView):
    model = Hat
    success_url = '/hats/'

