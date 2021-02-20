import uuid
import boto3

from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Petrock, Hat, Photo
from .forms import FeedingForm

S3_BASE_URL = 'https://s3.us-east-2.amazonaws.com/'
BUCKET = 'petrock-collector'

# Create your views here.
def home(request): 
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def petrocks_index(request):
    petrocks = Petrock.objects.all()
    return render(request, 'petrocks/index.html', { 'petrocks': petrocks })

@login_required
def petrocks_detail(request, petrock_id):
    petrock = Petrock.objects.get(id=petrock_id)
    hats_petrock_doesnt_have = Hat.objects.exclude(id__in = petrock.hats.all().values_list('id'))
    feeding_form = FeedingForm()
    return render(request, 'petrocks/detail.html', { 
        'petrock': petrock,
        'feeding_form': feeding_form,
        'available_hats': hats_petrock_doesnt_have
    })

@login_required
def add_feeding(request, petrock_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.petrock_id = petrock_id
        new_feeding.save()
    return redirect('petrocks_detail', petrock_id=petrock_id)

@login_required
def associate_hat(request, petrock_id, hat_id):
    Petrock.objects.get(id=petrock_id).hats.add(hat_id)
    return redirect('petrocks_detail', petrock_id=petrock_id)

@login_required
def unassociate_hat(request, petrock_id, hat_id):
    Petrock.objects.get(id=petrock_id).hats.remove(hat_id)
    return redirect('petrocks_detail', petrock_id=petrock_id)

@login_required
def add_photo(request, petrock_id):
    photo_file = request.FILES.get('photo_file', None)

    if photo_file:
        s3 = boto3.client('s3')
        index_of_last_period = photo_file.name.rfind('.')
        key = uuid.uuid4().hex[:6] + photo_file.name[index_of_last_period:]

        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"

            photo = Photo(url=url, petrock_id=petrock_id)
            photo.save()
        except:
            print('An error occurred uploading files to AWS')

    return redirect('petrocks_detail', petrock_id=petrock_id)

class PetrockCreate(LoginRequiredMixin, CreateView):
    model = Petrock
    fields = '__all__'

class PetrockUpdate(LoginRequiredMixin, UpdateView):
    model = Petrock
    fields = ['rockType', 'description', 'personality']

class PetrockDelete(LoginRequiredMixin, DeleteView):
    model = Petrock
    success_url = '/petrocks/'

class HatList(LoginRequiredMixin, ListView):
    model = Hat

class HatDetailView(LoginRequiredMixin, DetailView):
    model = Hat

class HatCreateView(LoginRequiredMixin, CreateView):
    model = Hat
    fields = '__all__'

class HatUpdateView(LoginRequiredMixin, UpdateView):
    model = Hat
    fields = '__all__'

class HatDeleteView(LoginRequiredMixin, DeleteView):
    model = Hat
    success_url = '/hats/'

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration /signup.html', context)
