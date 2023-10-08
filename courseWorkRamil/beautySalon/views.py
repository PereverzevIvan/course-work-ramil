import json
from django.http import HttpResponse, JsonResponse
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
    services = Service.objects.all()
    return render(request, 'show_all_services.html', {'services': services})

def show_one_service(request, service_id):
    pass


def show_user_profile(request, user_id: int):
    user = get_object_or_404(User, pk=user_id)

    context = {'human': user}

    if Master.objects.filter(user_id=user_id).exists():
        context['master'] = get_object_or_404(Master, user_id=user_id)
        
    return render(request, 'user_profile.html', context=context)


def set_rating(request):
    if request.method == 'GET':
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            message = 'Это сообщение от сервера! У тебя получилось!'
            return JsonResponse({'message': message})
    if request.method == 'POST':
        message = ''
        data = json.loads(request.body)
        old_rating = MasterRating.objects.filter(evaluating_id=data['evaluating'], evaluated_id=data['evaluated'])

        if old_rating:
            old_rating.delete()
            message = data['action'] + ' delete'
        else:
            new_rating = MasterRating()
            new_rating.evaluating_id = data['evaluating']
            new_rating.evaluated_id = data['evaluated']
            new_rating.value = 1 if data['action'] == 'like' else -1
            message = data['action']
            new_rating.save()

        return JsonResponse({'message': message})