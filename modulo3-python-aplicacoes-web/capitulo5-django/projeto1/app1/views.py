from django.shortcuts import render
from .forms import UserForm


def index(request):
    return render(request, 'user/index.html')

def create(request):

    if request.method == 'GET':
        form = UserForm()

        context = {
            'form': form,            
        }
        return render(request, 'user/criar.html', context=context)
