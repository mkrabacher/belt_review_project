# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import *
from datetime import datetime
import bcrypt
from django.db.models import Count
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm

def index(request):
    context = {
        'users':User.objects.all(),
        'regForm':RegistrationForm(),
        'loginForm':LoginForm()
    }
    return render(request, 'users/index.html', context)

def userPage(request, number):
    context = {
        'user':User.objects.get(id=number),
        'user_count':len(User.objects.get(id=number).reviews_given.all())
    }
    return render(request, 'users/user.html', context)

def registerUser(request):
    if request.method == "POST":
        response_form = RegistrationForm(request.POST)
        if response_form.is_valid():
            username = response_form.cleaned_data['username']
            first_name = response_form.cleaned_data['first_name']
            last_name = response_form.cleaned_data['last_name']
            email = response_form.cleaned_data['email']
            birthday =response_form.cleaned_data['birthday']

        password =response_form.cleaned_data['password']
        pw_conf = response_form.cleaned_data['confirm_password']
        if password != pw_conf:
            response_form.errors['password_match'] = "Your passwords don't match. Learn to type better"
        try:
            User.objects.get(email=email)
            response_form.errors['password_match'] = "Email is already taken. Be more creative than you are."
        except:
            pass
        if len(response_form.errors) > 0:
            if 'birthday' in response_form.errors:
                response_form.errors['birthday'] = 'Enter a valid birthday. Use **/**/**** format.'

            for tag, error in response_form.errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('/')

        else:
            User.objects.create(username=username, first_name=first_name, last_name=last_name, email=email, birthday=birthday, password=bcrypt.hashpw(password.encode(), bcrypt.gensalt()))
            messages.add_message(request, messages.INFO, 'Success. Now log in.')
            return redirect('/')

def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        
        try:
            user = User.objects.get(email=email)
        except:
            messages.add_message(request, messages.INFO, 'Email does not exist. you suck.')
            return redirect('/')

        if bcrypt.checkpw(password.encode(), user.password.encode()):
            request.session['curr_user_id'] = user.id
            return redirect('/books')

def logout(request):
    request.session.clear()
    return redirect('/')