# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponseRedirect
from .form import *
from .models import *
from django.contrib.auth.models import User
# Create your views here.


def login_view(request):
    error = None
    if request.user.is_authenticated:
        return HttpResponseRedirect("/")
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("inbox/")
        else:
            error = 'username or password is incorrect'

    template_name = 'registration/login.html'
    context = {
        'error': error
        }
    return render(request, template_name, context)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/accounts/login/")




def home(request):
    if request.user.is_authenticated:
        queryset = Message.objects.filter(reciever__username__iexact = request.user)
        context = {'user': request.user, 'object_list': queryset}

        template_name = 'messages.html'
        return render(request, template_name, context)
    return HttpResponseRedirect("/accounts/login/")

def register(request):
    message = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/accounts/login/")
    else:
        form = SignUpForm()

    template_name = 'registration/register.html'
    context = {
        "form": form,
    }
    return render(request, template_name, context)


def send_message(request):
    queryset = User.objects.all()

    form    = GetMessageForm()
    confirm = None
    if request.method == "POST":
        form = GetMessageForm(request.POST )
        print("post")
        if form.is_valid():
            reciever = request.POST.get("reciever")
            print(reciever)
            obj = Message.objects.create(
                reciever        = User.objects.get(username = reciever ),
                message_content = form.cleaned_data.get("message_content"),
                sender          = request.user

            )
            confirm = 'message sent successfuly'
    template_name = 'send_message.html'
    context = { 'object_list': queryset ,"form": form ,"confirm": confirm}
    return render(request,template_name,context)



def dbdump(request):
    if request.user.is_authenticated:
        context = {}

        template_name = 'db_dump.html'
        return render(request, template_name, context)
    return HttpResponseRedirect("/accounts/login/")







