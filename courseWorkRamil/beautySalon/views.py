from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, HttpResponsePermanentRedirect
from .models import *
from pprint import pprint

# Create your views here.
def index(request):
    return render(request, 'main_page.html')


def error_404(request, exception):
    data = {
        'exception': exception
    }
    return render(request,'404.html', data)


def show_all_masters(request):
    masters = Master.objects.all()
    
    return render(request, 'show_all_masters.html', {'masters': masters})


def show_all_services(request):
    pass

def show_one_service(request):
    pass


def show_user_profile(request, user_id: int):
    user = get_object_or_404(User, pk=user_id)

    context = {'human': user}

    if Master.objects.filter(user_id=user_id).exists():
        context['master'] = get_object_or_404(Master, user_id=user_id)
        context['specialization'] =  context['master'].specialization.all()
        

    return render(request, 'user_profile.html', context=context)

