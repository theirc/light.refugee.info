from django.shortcuts import redirect
from simple_ui.views import find_language


def redirect_to_home(request):
    return redirect('/' + find_language(request))
