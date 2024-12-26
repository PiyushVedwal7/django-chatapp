from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import RoomForm
from django.contrib import messages
from .models import Room,Topic
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import authenticate,logout,login


rooms = [
    {'id': 1, 'name': 'Lets learn python!'},
     {'id': 2, 'name': 'Design with me'},
     {'id': 3, 'name': 'Frontend developers'},
 ]



# Create your views here.
""""
def home(request):
    context={'rooms':rooms}
    return render(request, 'base/home.html',context)

def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room': room}
    return render(request, 'base/room.html', context)
    """
def home(request):
    #rooms = Room.objects.all()
    q = request.GET.get('q') if request.GET.get('q') else '' 
    rooms = Room.objects.filter(topic__name__icontains=q)
    room_count=rooms.count()


    rooms = Room.objects.filter(
    Q(topic__name__icontains=q) |
    Q(name__icontains=q) |
    Q(description__icontains=q)
)




    topics=Topic.objects.all()
    context = {'rooms': rooms,'topics':topics,'room_count':room_count}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)



@login_required(login_url='/login')
def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/room_form.html', context)


@login_required(login_url='/login')
def updateRoom(request, pk):
    # Retrieve the room object to be updated
    room = Room.objects.get(id=pk)
    # Prepopulate the form with the current room data
    form = RoomForm(instance=room)

    if request.user != room.host:
       return HttpResponse('You are not allowed here!')



    if request.method == 'POST':
        # Populate the form with submitted data and associate it with the room instance
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            # Save the updated room data
            form.save()
            return redirect('home')  # Redirect to the home page after saving

    context = {'form': form}
    return render(request, 'base/room_form.html', context)



"""
def loginPage(request):


    if request.method == 'POST':
       username = request.POST.get('username')
       password = request.POST.get('password')

    try:
        user = User.objects.get(username=username)
    except:
        messages.error(request, 'User does not exist')

    user = authenticate(request, username=username, password=password)

    if user is not None:
       login(request, user)
       return redirect('home')
    else:
        messages.error(request, 'Username OR password does not exit')    

    context = {}
    return render(request, 'base/login_register.html', context)
"""

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Replace 'home' with your desired redirect URL
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Both username and password are required')

    return render(request, 'base/login_register.html')  


def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': room})



def logoutUser(request):
    logout(request)
    return redirect('home')