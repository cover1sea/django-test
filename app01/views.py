from django.http import HttpResponse

# Create your views here.
def index(request):
    str_out = ""
    str_out += "<p>*** app01 *** start ***</p>"
    str_out += "<p>Hello. </p>"
    str_out += "<p>Nov/15 AM 09:45 </p>"
    str_out += "<p><a href='../'>Return</a></p>"
    str_out += "<p>*** app01 *** end ***</p>"
    return HttpResponse(str_out)