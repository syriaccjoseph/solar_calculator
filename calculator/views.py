# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import AreaForm 

def calculator(request):
    area = ''
    energy = ''
    template = loader.get_template('calculator/calculator.html')
    if request.method == 'POST':
        form = AreaForm(request.POST)
        if form.is_valid():
            # E = A * r * H * PR
            # E = Energy (kWh) 
            # A = Total solar panel Area (m2) 
            # r = solar panel yield or efficiency(%) 
            # H = Annual average solar radiation on tilted panels (shadings not included)
            # PR = Performance ratio, coefficient for losses (range between 0.5 and 0.9, default value = 0.75)
            area = form.cleaned_data['area']
            a = float(area)
            r = 15.0
            h = 1361.0
            pr = 0.75
            e = a * r * h * pr
            area = str(a)
            energy = str(e)
        else:
            context = {
                'error_message' : 'Enter a floating-point number'
            }
            return HttpResponse(template.render(context, request))

    context = {
        'area': area,
        'nominal_power': energy,
    }

    return HttpResponse(template.render(context, request))

