from django.shortcuts import redirect

def calculator_redirect(request):
    response = redirect('/calculator/')
    return response