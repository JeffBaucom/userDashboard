from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from models import *

#----------- Sign in & registration methods -------------

def index(request):
    # Display welcome page

    return render(request, 'dashboard/index.html')

def register(request):
    # Display register page

    return render(request, 'dashboard/register.html')

def validate(request):
    # Validates registration/login form data & redirects to user's dashboard or admin dashboard
    errors = User.objects.registration_validator(request.POST)
    if len(errors):
        for tag, error, in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
            print messages
    return redirect('dash_admin')
    #return redirect('dash')

def signin(request):
    # Sign in page
    # Redirect to respecitve user/admin dashboard if already signed in

    return render(request, 'dashboard/signin.html')


#--------------- Admin page and methods ---------------

def dash_admin(request):
    # Admin's dashboard

    return render(request, 'dashboard/admin.html')

def admin_users_new(request):
    # Admin's 'add new user' form

    return render(request, 'dashboard/new-user.html')

def users_new_process(request):
    # 'add new user' form validation

    return redirect('dash_admin')

def admin_edit(request, id):
    # Admin's 'edit user' form

    return render(request, 'dashboard/edit-admin.html')

def admin_edit_process(request, id):
    # 'edit user' from validation

    return redirect('dash_admin')

def admin_remove_user(request):
    # removes user, maybe add a confirmation page?

    return redirect('dash_admin')


#----------------- User page and methods -------------------

def users_show(request, id):
    # Display user's wall

    return render(request, 'dashboard/show-user.html')

def dash(request):
    # Display user's dashboard

    return render(request, 'dashboard/dashboard.html')

def user_edit(request):
    # Display form to edit user's own profile

    return render(request, 'dashboard/edit-user.html')

def user_edit_process(request):
    # Validate user's edits

    return redirect('dash')

def logout(request):
    # Logs user out

    return redirect('dash_index')
