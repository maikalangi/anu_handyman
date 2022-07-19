from pyexpat import model
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import FormView
from .models import Contact

# Create views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contactView(request):
    if request.method == 'GET':
        form = Contact()
    else:
        form = Contact(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(
                    subject, 
                    message, 
                    email, 
                    ['maikalangi@gmail.com'], 
                    fail_silently=False,
                )
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return redirect('success')
    return render(request, 'contacts/contact.html', {'form': form})

def successView(request):
    return render(request, 'contacts/contact_success.html')

# class ContactForm(FormView):
#     model = Contact
#     template_name = 'contacts/contact.html'
#     form_class = ContactForm
#     success_url = '/'