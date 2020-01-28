# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def index(request, area):

    # E = A * r * H * PR
    # E = Energy (kWh) 
    # A = Total solar panel Area (m2) 
    # r = solar panel yield or efficiency(%) 
    # H = Annual average solar radiation on tilted panels (shadings not included)
    # PR = Performance ratio, coefficient for losses (range between 0.5 and 0.9, default value = 0.75)
    
    a = float(area)
    r = 15.0
    h = 1361.0
    pr = 0.75

    e = a * r * h * pr

    return HttpResponse("Nominal power : " + str(e))

# Create your views here.
