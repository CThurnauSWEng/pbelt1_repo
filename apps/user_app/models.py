from __future__ import unicode_literals
from django.db import models


import re
import bcrypt

NAME_REGEX = re.compile(r'^[A-Za-z ]*$')

# model manager and validators 
class UserManager(models.Manager):
    def validate_registration_data(self, post_data):
        response = {
            'status' : True
        }
        errors = []

        if len(post_data['name']) < 3:
            errors.append("Name must be at least 3 characters long")

        if not re.match(NAME_REGEX, post_data['name']):
            errors.append('Name may only contain characters')

        if len(post_data['username']) < 3:
            errors.append("Username must be at least 3 characters long")

        if not re.match(NAME_REGEX, post_data['username']):
            errors.append('User name may only contain characters')

        if len(post_data['password']) < 8:
            errors.append("Password must be at least 8 characters long")

        if post_data['password'] != post_data['pw_confirm']:
            errors.append("Passwords do not match!")

        if len(errors) > 0:
            response['status'] = False
            response['errors'] = errors
        else:
            hashedpwd = bcrypt.hashpw((post_data['password'].encode()), bcrypt.gensalt(5))

            user = User.objects.create(
                        name       = post_data['name'],
                        username   = post_data['username'],
                        password   = hashedpwd)

            response['user'] = user
            
        return response

    def validate_login_data(self, post_data):
        response = {
            'status' : True
        }
        errors = []
        hashedpwd = bcrypt.hashpw((post_data['password'].encode()), bcrypt.gensalt(5))

        user = User.objects.filter(username = post_data['username'])

        if len(user) > 0:
            # check this user's password
            user = user[0]
            if not bcrypt.checkpw(post_data['password'].encode(), user.password.encode()):
                errors.append('username/password incorrect')
        else:
            errors.append('username/password incorrect')

        if len(errors) > 0:
            response['status'] = False
            response['errors'] = errors
        else:
            response['user'] = user
        return response

class TripManager(models.Manager):
    def validate_trip_data(self, post_data):
        print "in validate_trip_date"

        response = {
            'status' : True
        }
        errors = []

        if len(post_data['name']) < 3:
            errors.append("Destination nane must be at least 3 characters long")

        if len(post_data['desc']) < 3:
            errors.append("Description must be at least 3 characters long")

        if len(post_data['planned_by']) < 3:
            errors.append("planned_by must be at least 3 characters long")

        # future enhancements:
        #   - add checks for valid date
        #   - add a check that from is after now
        #   - add a check that from is earlier than to

        if len(errors) > 0:
            response['status'] = False
            response['errors'] = errors
        else:

            trip = Trip.objects.create(
                        name       = post_data['name'],
                        desc       = post_data['desc'],
                        planned_by = post_data['planned_by'])
                        # date_from  = post_data['date_from'],
                        # date_to     = post_data['date_to'])

            response['trip'] = trip

            # link this user to this trip
            user_id = post_data['user_id']
            print "user_id", user_id
            this_user = User.objects.get(id=user_id)

            this_user.trips.add(trip)
            
        return response


# database models
class Trip(models.Model):
    name        = models.CharField(max_length=255)
    desc        = models.CharField(max_length=255)
    planned_by  = models.CharField(max_length=255)
    date_from   = models.DateField(auto_now_add=True)
    date_to     = models.DateField(auto_now_add=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now_add=True)
    objects     = TripManager()

class User(models.Model):
    name        = models.CharField(max_length=255)
    username    = models.CharField(max_length=255)
    password    = models.CharField(max_length=255)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now_add=True)
    trips       = models.ManyToManyField(Trip, related_name="travelers")
    objects     = UserManager()




