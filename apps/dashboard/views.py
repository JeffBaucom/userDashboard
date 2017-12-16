from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from models import *

def index(request):
    return render(request, 'dashboard/index.html')

def register(request):

    return render(request, 'dashboard/register.html')

def register_check(request):

    return redirect(request, 'dashboard/')

def signin(request):

    return render(request, 'dashboard/signin.html')

def signin_check(request):

    return redirect('show_user', id)
    return redirect('dash_admin')

# admin page and methods

def dash_admin(request):

    return render(request, 'dashboard/admin.html')

def users_new(request):

    return render(request, 'dashboard/new-user.html')

def users_new_process(request):

    return redirect('dash_admin')

def admin_edit(request, id):

    return render(request, 'dashboard/edit-admin.html')

def admin_edit_process(request, id):

    return redirect('dash_admin')

# user page and methods

def users_show(request, id):

    return render(request, 'dashboard/show-user.html')

def dash(request):

    return render(request, 'dashboard/dashboard.html')

def user_edit(request):

    return render(request, 'dashboard/edit-user.html')

def user_edit_process(request):

    return redirect('dash')
