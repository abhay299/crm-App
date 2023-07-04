from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SingnUpForm
from .models import Record
# Create your views here.


def home(request):
    records = Record.objects.all()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect('home')
        else:
            messages.success(
                request, "There was an error loggin In, please try again...")
            return redirect('home')
    else:
        return render(request, 'home.html', {'records': records})


def logoutUser(request):
    logout(request)
    messages.success(request, "You have been logged out...")
    return redirect('home')


def registerUser(request):
    if request.method == "POST":
        form = SingnUpForm(request.POST)
        if form.is_valid():
            form.save()

            # Authenticate and Login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have successfully registered!")
            return redirect('home')

    else:
        form = SingnUpForm()
        return render(request, 'register.html', {'form': form})

    return render(request, 'register.html', {'form': form})


def customerRecord(request, pk):
    if request.user.is_authenticated:
        # Look up records
        customerRecord = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customerRecord': customerRecord})
    else:
        messages.success(request, "You must login to view that page...")
        return redirect('home')


def deleteRecord(request, pk):
    if request.user.is_authenticated:
        deleteData = Record.objects.get(id=pk)
        deleteData.delete()
        messages.success(request, "Request Deleted Successfully!")
        return redirect("home")
    else:
        messages.success(request, "You must be logged in to do that.")
        return redirect('home')


def addRecord(request):
    return render(request, 'addRecord.html', {})
