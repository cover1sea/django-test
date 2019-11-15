from django.http import HttpResponse

# Create your views here.
def index(request):
    str_out = ""
    str_out += "<p>*** app02 *** start ***</p>"
    str_out += "<p>Good morning. </p>"
    str_out += "<p>Nov/15 AM 09:55 </p>"
    str_out += "<p><a href='../'>Return</a></p>"
    str_out += "<p>*** app02 *** end ***</p>"
    return HttpResponse(str_out)