from pyexpat import model
from django.shortcuts import render
from django.views.generic import FormView
from .models import ContactForm, Contact

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

class ContactForm(FormView):
    model = Contact
    template_name = 'contacts/contact.html'
    form_class = ContactForm