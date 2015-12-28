from django.http import HttpResponse
from django.shortcuts import render

from .models import UnprocessedImg, ProcessedImg

# Create your views here.


def index(request):
    return render(request, 'imgapp/index.html', {})


def unprocessed_img(request):
    unprocessed_list = UnprocessedImg.objects.all()
    return render(request, 'imgapp/unprocessed.html', {'unprocessed_list': unprocessed_list})


def unprocessed_serial_search(request, serial):
    unprocessed_list = UnprocessedImg.objects.filter(serial__exact=serial)
    return render(request, 'imgapp/unprocessed.html', {'unprocessed_list': unprocessed_list})


def processed_img(request):
    processed_list = ProcessedImg.objects.all()
    return render(request, 'imgapp/processed.html', {'processed_list': processed_list})


def processed_serial_search(request, serial):
    processed_list = ProcessedImg.objects.filter(serial__exact=serial)
    return render(request, 'imgapp/processed.html', {'processed_list': processed_list})
