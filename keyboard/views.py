from django.shortcuts import render, get_object_or_404
from .models import KeyboardName, KeyboardReview, KeyboardType
from django.urls import reverse_lazy
from .forms import KeyboardForm, KeyboardImageForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'keyboard/index.html')

def keyboardname(request):
    name_list=KeyboardName.objects.all()
    return render(request, 'keyboard/keyboardname.html', {'name_list': name_list})

def keyboardimage(request):
    image_list=KeyboardReview.objects.all()
    return render(request, 'keyboard/keyboardimage.html', {'image_list' : image_list})

def keyboardDetail(request, id):
    keyboard=get_object_or_404(KeyboardName, pk=id)
    return render(request, 'keyboard/keyboarddetail.html', {'keyboard' : keyboard})

@login_required
def newKeyboard(request):
    form=KeyboardForm

    if request.method=='POST':
        form=KeyboardForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=KeyboardForm()
    else:
        form=KeyboardForm()
    return render(request, 'keyboard/newkeyboard.html', {'form' : form})

@login_required
def newKeyboardImage(request):
    form=KeyboardImageForm

    if request.method=='POST':
        form=KeyboardImageForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=KeyboardImageForm()
    else:
        form=KeyboardImageForm()
    return render(request, 'keyboard/newkeyboardimage.html', {'form' : form})

def loginmessage(request):
    return render(request, 'keyboard/loginmessage.html')

def logoutmessage(request):
    return render(request, 'keyboard/logoutmessage.html')