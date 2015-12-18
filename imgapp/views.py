import os
import os.path

from django.http import HttpResponse
from django.shortcuts import render

from pyftpdlib.handlers import FTPHandler

from .models import UnprocessedImg

# Create your views here.


def index(request):
    return HttpResponse("Hello world. This is the index.")


class FTPHandle(FTPHandler):

    def on_file_received(self, file):
        base = os.path.basename(file)
        serial, ext = os.path.splitext(base)
        if(ext == '.jpg'):
            img = UnprocessedImg(path=file, serial=serial)
            img.save()
        else:
            os.remove(file)

    def on_incomplete_file_received(self, file):
        os.remove(file)