from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(request):
    dd = {
            'hour': datetime.now().hour,
            'minute': datetime.now().minute,
            'message': 'Message from app01.',
    }
    return render(request,'app01/app01.html', dd)
