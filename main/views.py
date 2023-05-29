from django.http import HttpResponse
from main.models import Flex


# Create your views here.
def index(request):
    try:
        data = Flex.objects.filter(message="hello world")
    except Exception:
        return HttpResponse("Data not found", status=500)
    return HttpResponse(data, status=200)
