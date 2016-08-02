from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from .models import UnprocessedImg, ProcessedImg

# Create your views here.


def index(request):
    return render(request, 'imgapp/index.html', {})


def do_sorting(hlist, qtype):
    if qtype[0] == "-":
        dec = True
        typeq = qtype[1:]
    else:
        dec = False
        typeq = qtype

    for i in hlist:
        if i['id'] == typeq:
            i['sort'] = True
            if not dec:
                i['glyph'] = "glyphicon glyphicon-triangle-top"

    return hlist


def db_unprocessed(request, match, qtype, param, sort):
    if match == "all" and qtype == "":
        rlist = UnprocessedImg.objects.all()
    elif match == "all" and qtype != "":
        rlist = UnprocessedImg.objects.all().order_by(sort)
    elif match == "exact" and qtype == "id":
        rlist = UnprocessedImg.objects.filter(id__exact=param).order_by(sort)
    elif match == "exact" and qtype == "ext":
        rlist = UnprocessedImg.objects.filter(ext__exact=param).order_by(sort)
    elif match == "exact" and qtype == "base":
        rlist = UnprocessedImg.objects.filter(base__exact=param).order_by(sort)
    elif match == "exact" and qtype == "serial":
        rlist = UnprocessedImg.objects.filter(serial__exact=param).order_by(sort)
    elif match == "exact" and qtype == "receive_date":
        rlist = UnprocessedImg.objects.filter(receive_date__exact=param).order_by(sort)
    elif match == "exact" and qtype == "receive_time":
        rlist = UnprocessedImg.objects.filter(receive_time__exact=param).order_by(sort)
    elif match == "exact" and qtype == "processed":
        rlist = UnprocessedImg.objects.filter(processed__exact=param).order_by(sort)
    else:
        return HttpResponseNotFound("<h1>Database query invalid.</h1>")

    hlist = [
        {
            "id": "id",
            "tag": "ID",
            "sort": False,
            "glyph": "glyphicon glyphicon-triangle-bottom",
        },
        {
            "id": "serial",
            "tag": "Serial",
            "sort": False,
            "glyph": "glyphicon glyphicon-triangle-bottom",
        },
        {
            "id": "processed",
            "tag": "Status",
            "sort": False,
            "glyph": "glyphicon glyphicon-triangle-bottom",
        },
        {
            "id": "receive_date",
            "tag": "Rcv Date",
            "sort": False,
            "glyph": "glyphicon glyphicon-triangle-bottom",
        },
        {
            "id": "receive_time",
            "tag": "Rcv Time",
            "sort": False,
            "glyph": "glyphicon glyphicon-triangle-bottom",
        },
        {
            "id": "local",
            "tag": "Local Exists",
            "sort": False,
            "glyph": "glyphicon glyphicon-triangle-bottom",
        },
    ]

    return render(request, 'imgapp/unprocessed.html', {'rlist': rlist, 'hlist': do_sorting(hlist, sort)})


def db_processed(request, match, qtype, param, sort):
    if match == "all" and qtype == "":
        rlist = ProcessedImg.objects.all()
    elif match == "all" and qtype != "":
        rlist = ProcessedImg.objects.all().order_by(sort)
    elif match == "exact" and qtype == "id":
        rlist = ProcessedImg.objects.filter(id__exact=param).order_by(sort)
    elif match == "exact" and qtype == "ext":
        rlist = ProcessedImg.objects.filter(ext__exact=param).order_by(sort)
    elif match == "exact" and qtype == "base":
        rlist = ProcessedImg.objects.filter(base__exact=param).order_by(sort)
    elif match == "exact" and qtype == "serial":
        rlist = ProcessedImg.objects.filter(serial__exact=param).order_by(sort)
    elif match == "exact" and qtype == "receive_date":
        rlist = ProcessedImg.objects.filter(finish_date__exact=param).order_by(sort)
    elif match == "exact" and qtype == "receive_time":
        rlist = ProcessedImg.objects.filter(finish_time__exact=param).order_by(sort)
    elif match == "exact" and qtype == "processed":
        rlist = ProcessedImg.objects.filter(processed__exact=param).order_by(sort)

    hlist = [
        {
            "id": "unprocessed.id",
            "tag": "ID",
            "sort": False,
            "glyph": "glyphicon glyphicon-triangle-bottom",
        },
        {
            "id": "unprocessed.serial",
            "tag": "Serial",
            "sort": False,
            "glyph": "glyphicon glyphicon-triangle-bottom",
        },
        {
            "id": "finish_date",
            "tag": "Finish Date",
            "sort": False,
            "glyph": "glyphicon glyphicon-triangle-bottom",
        },
        {
            "id": "finish_time",
            "tag": "Finish Time",
            "sort": False,
            "glyph": "glyphicon glyphicon-triangle-bottom",
        },
        {
            "id": "local",
            "tag": "Local Exists",
            "sort": False,
            "glyph": "glyphicon glyphicon-triangle-bottom",
        },
    ]

    return render(request, 'imgapp/processed.html', {'rlist': rlist, 'hlist': do_sorting(hlist, sort)})


def db_query(request, mreq, match, qtype, param, sort):
    if mreq == "unprocessed":
        return db_unprocessed(request, match, qtype, param, sort)
    elif mreq == "processed":
        return db_processed(request, match, qtype, param, sort)
    else:
        return HttpResponseNotFound("<h1>Database table does not exist.</h1>")
