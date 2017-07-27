# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from learn_app.reverse_models import DownloadQueue
from learn_app.reverse_models import LearnAppPerson

def index(request):
    # data = request.POST
    return HttpResponse("hello")

def add(request):
    a = request.GET.get('a', 0)
    b = request.GET.get('b', 0)
    c = int(a) + int(b)
    return HttpResponse(str(c))

def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))

@csrf_exempt
def amazon(request):

    # return HttpResponse(u"你好, 这个是Django框架测试!!!!!!!!---")

    if (request.method == 'GET'):
        return HttpResponse(request.method)
    elif (request.method == 'POST'):
        # return HttpResponse("POST method")
        post_data = request.POST["data"]
        access_key = request.POST["access_key"]
        if (access_key == "ABCDEFG"):
            # print (type(post_data))
            data = json.loads(post_data)
            # print (data)
            responses = {}
            response = {}
            try:
                for key, value in data.items():
                    ac_download_queue_id = value["id"]
                    region = value["region"]
                    type = value["type"]
                    v = value["value"]
                    p1 = DownloadQueue(region=region, type=type, value=v, ac_download_queue_id=ac_download_queue_id, status=0, priority=0, scrape_count=0, upload_status=0, upload_count=0)
                    p1.save()
                    response[key] = p1.id
                    # print (value)
                responses['data'] = response
                responses['success'] = True
                return HttpResponse(json.dumps(responses))
            except Exception as err:
                print (err)
        else:
            return HttpResponse("access_key wrong")
        # received_json_data = json.loads(request.body)
    else:
        return HttpResponse("wrong")
