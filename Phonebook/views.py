from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from Phonebook.serializer import ContactSerializer

from django.core.files.storage import default_storage

# Create your views here
"""
def contact_list(request):
    contacts = Contact.objects.all()
    contacts_serializer = ContactSerializer(contact, many = True)
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
"""


@csrf_exempt    
def contact_api(request, id = 0):
    if request.method == 'GET':
        contact = Contact.objects.all()
        contact_serializer = ContactSerializer(contact, many = True)
        return JsonResponse(contact_serializer.data, safe = False)
    
    elif request.method == 'POST':
        contact_data = JSONParser().parse(request)
        contact_serializer = ContactSerializer(data = contact_data)
        if contact_serializer.is_valid():
            contact_serializer.save()
            return JsonResponse("Contact Added Successfully", safe = False)
        return JsonResponse("Contact Failed to add", safe = False)
    
    elif request.method == 'PUT':
        contact_data = JSONParser().parse(request)
        contact = Contact.objects.get(name = contact_data['name'])
        contact_serializer = ContactSerializer(contact, data = contact_data)
        if contact_serializer.is_valid():
            contact_serializer.save()
            return JsonResponse("Contact updated Successfully", safe = False)
        return JsonResponse("Contact failed to Update", safe = False)
    
    elif request.method == 'DELETE':
        contact = Contact.objects.get(id = id)
        contact.delete
        return JsonResponse("Contact Deleted Successfully", safe = False)