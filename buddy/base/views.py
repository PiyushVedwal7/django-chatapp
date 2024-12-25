from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import RoomForm
from .models import Room


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
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)

def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/room_form.html', context)

def updateRoom(request, pk):
    # Retrieve the room object to be updated
    room = Room.objects.get(id=pk)
    # Prepopulate the form with the current room data
    form = RoomForm(instance=room)

    if request.method == 'POST':
        # Populate the form with submitted data and associate it with the room instance
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            # Save the updated room data
            form.save()
            return redirect('home')  # Redirect to the home page after saving

    context = {'form': form}
    return render(request, 'base/room_form.html', context)



def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': room})