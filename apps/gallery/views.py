from django.http import HttpResponse

def gallery_view(request):
    return HttpResponse("I am gallery")

def album_detail(request, pk):
    return HttpResponse(f"I am album {pk}")