from django.shortcuts import (render, redirect,
                              HttpResponseRedirect,
                              get_object_or_404)
from django.http import (HttpResponse,
                         Http404)

from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import ListForm, LoginForm
from .models import Client



def add_client(request):
    if request.method == 'POST':
        form = ListForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ListForm()
    return render(request, 'list2.html', {'form': form})


def success(request):
    return HttpResponse('successfully uploaded')

def ListClient(request):
    model = Client.object.all()
    context = {'client':model}
    return render(request, 'list.html', context)

def detail_product(request, client_id):
    try:
        client = Client.object.get(pk=client_id)

    except ObjectDoesNotExist:
        raise Http404("Client does not exist")
    return render(request, 'detail_client.html', {'product': client})



def delete_view(request, client_id):
    context = {}
    client = Client.object.get(pk=client_id)
    if request.method == 'POST':
        client.delete()
    return render(request, 'delete_client.html', context)

def update_view(request, id):
    context = {}

    # fetch(download) the object related to passed id
    obj = get_object_or_404(Client, id=id)

    # pass the object as instance in form
    form = ListForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")

    context = {"form": form}
    return render(request, "updateclient.html", context)

def get_redirect_if_exists(request):
    redirect = None
    if request.GET:
        if request.GET.get("next"):
            redirect = str(request.GET.get("next"))
    return redirect


def login_view(request):
    if request.POST:

        email = request.POST['email']
        password = request.POST['password']
        print(email, password)
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('delete')

        else:
            return render(request, 'login.html')
    form = AuthenticationForm()
    return render(request, 'login.html', { 'form':form})



