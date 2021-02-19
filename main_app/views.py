from django.shortcuts import render, redirect
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

def add_feeding(request, petrock_id):
    form = FeedingForm(request.post)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.petrock_id = petrock_id
        new_feeding.save()
    return redirect('detail', petrock_id=petrock_id)

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

