from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm

# Create your views here.
def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, "Phonebook/contact_list.html", {'contacts': contacts})

def contact_form(request, id = 0):
    if request.method == "GET":
        if id == 0:
            form = ContactForm()
        else:
            contact = Contact.objects.get(pk=id)
            form = ContactForm(instance = contact)
        return render(request,"Phonebook/contact_form.html", {'form': form})
    else:
        if id == 0:
            form = ContactForm(request.POST)
        else:
            contact = Contact.objects.get(pk=id)
            form = ContactForm(request.POST,instance = contact)
        if form.is_valid():
            form.save()
        return redirect('/contact/list')

def contact_delete(request, id):
    contact = Contact.objects.get(pk=id)
    contact.delete()
    return redirect('/contact/list')