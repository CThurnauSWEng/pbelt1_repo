from django.shortcuts import render, HttpResponse, redirect

# the welcome_traveler function is called when the user logs in or registers
def welcome_traveler(request):
    print "about to render template welcome.html"
    return render(request, "travel_app/welcome.html")


# Rats, even though I made this work in both belt reviewer and user dashboard, I
# can't figure out why I get a render template error above. 
# Guess I'm just freezing up. Have spent 30 minutes
# trying to debug, must move on now, so I will proceed with just one app