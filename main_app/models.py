from django.db import models
from django.forms import ModelForm

# Create your models here.

class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.email

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'