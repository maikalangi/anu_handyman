from django.db import models
from django.forms import ModelForm
from django import forms

# Create your models here.

class Contact(forms.Form):
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    def __str__(self):
        return self.email

# class Contact(models.Model):
#     email = models.EmailField()
#     subject = models.CharField(max_length=255)
#     message = models.TextField()

#     def __str__(self):
#         return self.email

# class ContactForm(ModelForm):
#     class Meta:
#         model = Contact
#         fields = '__all__'