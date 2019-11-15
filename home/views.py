from django.http import HttpResponse

# Create your views here.
def index(request):
    str_out = ""
    str_out += "<p>*** home *** start ***</p>"
    str_out += "<p>This is Home. </p>"
    str_out += "<p><a href='app01/'>app01</a></p>"
    str_out += "<p><a href='app02/'>app02</a></p>"
    str_out += "<p>*** home *** end ***</p>"
    return HttpResponse(str_out)