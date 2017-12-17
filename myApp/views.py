# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

# Create your views here.


@csrf_exempt
def get_filelist(request):
    with open(r"frontWeb\static\filelist.txt", 'r') as f_w:
        response = {}
        data_list = []
        for line in f_w.readlines():
            json_data = {}
            json_data['filename'] = line
            data_list.append(json_data)
        response['filelist'] = data_list
	return JsonResponse(response)
