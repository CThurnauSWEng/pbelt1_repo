from django.shortcuts import render, HttpResponse, redirect
from .models import User,Trip
from django.contrib import messages

import bcrypt


# Create your views here.
def index(request):
    if not 'errors' in request.session:
        request.session['errors']  = []
    return render(request, "user_app/index.html")

def user_create(request):
    
    # the method validate_registration_data validates the form data and if there
    # are no errors, it also creates the user and returns the user object.
    # if there are errors, it returns a list of them in the response object.

    response = User.objects.validate_registration_data(request.POST)

    if (response['status']):
        request.session['errors']  = []

        request.session['user_id'] = response['user'].id

        return redirect('/travels')
    else:
        request.session['errors'] = response['errors']
        return redirect('/')

def add_trip(request):
    return render(request, "user_app/add_trip.html")

def create_trip(request):
    print "in views create_trip"
    print "request.POST", request.POST
    print "request.POST['name']:", request.POST['name']
    response = Trip.objects.validate_trip_data(request.POST)
    if (response['status']):
        request.session['errors']  = []
        return redirect('/travels')
    else:
        request.session['errors'] = response['errors']
        return redirect('/')

def show_trip(request, trip_id):

    trip = Trip.objects.get(id=trip_id)

    context = {
        'trip' : trip
    }

    return render(request, "user_app/show_trip.html", context)

def travels(request):

    this_user = User.objects.get(id=request.session['user_id'])
    this_users_trips = this_user.trips.all()

    for trip in this_users_trips:
        print "trip_name: ",trip.name

    # not fully implemented:
    other_users_trips = Trip.objects.all()

    context = {
        'user'  : this_user,
        'trips' : this_users_trips,
        'other_trips' : other_users_trips
    }

    return render(request, "user_app/welcome.html",context)


def user_login(request):
    
    # the method validate_registration_data validates the form data and if there
    # are no errors, it also creates the user and returns the user object.
    # if there are errors, it returns a list of them in the response object.

    response = User.objects.validate_login_data(request.POST)

    if (response['status']):

        request.session['errors']  = []
        request.session['user_id'] = response['user'].id

        return redirect('/travels')
    else:
        request.session['errors'] = response['errors']
        return redirect('/')

def user_logout(request):
    request.session['name'] = ""
    request.session['user_id'] = ""
    return redirect('/')

