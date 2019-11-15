from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(request):
    dd = {
            'hour': datetime.now().hour,
            'minute': datetime.now().minute,
            'message': 'Message from app02.',
    }
    return render(request,'app02/app02.html', dd)
