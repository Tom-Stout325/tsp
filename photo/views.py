from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect, BadHeaderError, HttpResponse
from .forms import ContactForm
from django.core.mail import send_mail
from django.views import generic
from .models import *
from django.contrib import messages
from django.template.loader import render_to_string
from django.contrib.auth.forms import AuthenticationForm



def AboutPage(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            contact_email = form.cleaned_data['contact_email']
            message = form.cleaned_data['message']

            html = render_to_string('components/contact_email.html', {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'message': message,
            })
            send_mail( 'Contact Form from' +':' + contact_name, contact_email, '{{ self.message }}' 'tom.stout325@gmail.com', ['tom@tom-stout.com'], html_message=html)
            messages.success(request, "Your message has been sent!")
            return redirect('thanks')
        
    else:
        form=ContactForm()
        return render(request, 'photo/about.html', { 'form': form })


def ClientPage(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            contact_email = form.cleaned_data['contact_email']
            message = form.cleaned_data['message']

            html = render_to_string('components/contact_email.html', {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'message': message,
            })
            send_mail( 'Contact Form from' +':' + contact_name, contact_email, '{{ self.message }}' 'tom.stout325@gmail.com', ['tom@tom-stout.com'], html_message=html)
            messages.success(request, "Your message has been sent!")
            return redirect('thanks')
     
    else:    
        form=ContactForm()
        return render(request, 'photo/clients.html', { 'form': form })


def ContactPage(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            contact_email = form.cleaned_data['contact_email']
            message = form.cleaned_data['message']

            html = render_to_string('components/contact_email.html', {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'message': message,
            })
            send_mail( 'Contact Form from' +':' + contact_name, contact_email, '{{ self.message }}' 'tom.stout325@gmail.com', ['tom@tom-stout.com'], html_message=html)
            messages.success(request, "Your message has been sent!")
            return redirect('thanks')
 
    else:    
        form=ContactForm()
        return render(request, 'photo/contact.html',  { 'form': form })


def DronePage(request):           
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            contact_email = form.cleaned_data['contact_email']
            message = form.cleaned_data['message']

            html = render_to_string('components/contact_email.html', {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'message': message,
            })
            send_mail( 'Contact Form from' +':' + contact_name, contact_email, '{{ self.message }}' 'tom.stout325@gmail.com', ['tom@tom-stout.com'], html_message=html)
            messages.success(request, "Your message has been sent!")
            return redirect('thanks')
    
    else:    
        form=ContactForm()
        return render(request, 'components/port_drone.html', { 'form': form })


def HomePage(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            contact_email = form.cleaned_data['contact_email']
            message = form.cleaned_data['message']

            html = render_to_string('components/contact_email.html', {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'message': message,
            })
            send_mail( 'Contact Form from' +':' + contact_name, contact_email, '{{ self.message }}' 'tom.stout325@gmail.com', ['tom@tom-stout.com'], html_message=html)
            messages.success(request, "Your message has been sent!")
            return redirect('thanks')
    
    else:    
        form=ContactForm()
        return render(request, 'photo/home.html', { 'form': form })
   

def InfoPage(request):    
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            contact_email = form.cleaned_data['contact_email']
            message = form.cleaned_data['message']

            html = render_to_string('components/contact_email.html', {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'message': message,
            })
            send_mail( 'Contact Form from' +':' + contact_name, contact_email, '{{ self.message }}' 'tom.stout325@gmail.com', ['tom@tom-stout.com'], html_message=html)
            messages.success(request, "Your message has been sent!")
            return redirect('thanks')
    
    else:    
        form=ContactForm()
        return render(request, 'photo/info.html', { 'form': form })
     

def SeniorsPage(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            contact_email = form.cleaned_data['contact_email']
            message = form.cleaned_data['message']

            html = render_to_string('components/contact_email.html', {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'message': message,
            })
            send_mail( 'Contact Form from' +':' + contact_name, contact_email, '{{ self.message }}' 'tom.stout325@gmail.com', ['tom@tom-stout.com'], html_message=html)
            messages.success(request, "Your message has been sent!")
            return redirect('thanks')
    
    else:    
        form=ContactForm()
        return render(request, 'components/port_seniors.html', { 'form': form })


class ThankYouView(generic.TemplateView):
    template_name = ('components/thank_you.html')


def WeddingsPage(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            contact_email = form.cleaned_data['contact_email']
            message = form.cleaned_data['message']

            html = render_to_string('components/contact_email.html', {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'message': message,
            })
            send_mail( 'Contact Form from' +':' + contact_name, contact_email, '{{ self.message }}' 'tom.stout325@gmail.com', ['tom@tom-stout.com'], html_message=html)
            messages.success(request, "Your message has been sent!")
            return redirect('thanks')
    
    else:    
        form=ContactForm()
        return render(request, 'components/port_weddings.html', { 'form': form })


def PortraitsPage(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            contact_email = form.cleaned_data['contact_email']
            message = form.cleaned_data['message']

            html = render_to_string('components/contact_email.html', {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'message': message,
            })
            send_mail( 'Contact Form from' +':' + contact_name, contact_email, '{{ self.message }}' 'tom.stout325@gmail.com', ['tom@tom-stout.com'], html_message=html)
            messages.success(request, "Your message has been sent!")
            return redirect('thanks')
    
    else:    
        form=ContactForm()
        return render(request, 'components/port_portraits.html', { 'form': form })