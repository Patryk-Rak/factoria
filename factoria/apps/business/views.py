from django.shortcuts import render
from django.http import HttpRequest, HttpResponse ,Http404
from django.core.exceptions import ObjectDoesNotExist

from .models import Business


def create_new_business(request:HttpRequest):
    new_business = Business(
        NIP=request.POST['NIP'],
        name=request.POST['name'],
        owner=request.POST['owner']
        )
    new_business.save()

def edit_business(request:HttpRequest,business:Business):
    business.NIP = request.POST['NIP']
    business.name = request.POST['name']
    business.owner = request.POST['owner']
    business.save()

##################### CRUD ########################
def create(request:HttpRequest):
    if request.method == 'GET':
        return render(request,'business/create.html')
    if request.method=="POST":
        create_new_business(request)
        return HttpResponse("Created New Business Success")

def retrive(request:HttpRequest):
    all_business = Business.objects.all()
    context = { 'dataset': all_business }
    return render(request,'website/business/business_list.html',context)

def update(request:HttpRequest,id):
    try:
        business = Business.objects.get(pk=id)
        if request.method == 'GET':
            return render(request,'business/update.html',{'business':business})
        if request.method == 'POST':
            edit_business(request,business)
            return HttpResponse("Updating Business Success")
    except ObjectDoesNotExist:
        return Http404("Business does not exist")
          
def delete(request:HttpRequest,id):
    try:
        business = Business.objects.get(pk=id)
        business.delete()
        return HttpResponse("Deleting Business Success")
    except ObjectDoesNotExist:
        return Http404("Business does not exist")
    
'''
How to heandel ERRORS
'''
