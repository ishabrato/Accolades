from django.http import HttpResponse

def member_list(request):
    return HttpResponse("I am members")

def member_profile(request, pk):
    return HttpResponse(f"I am member profile {pk}")