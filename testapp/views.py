from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Count

# @csrf_exempt
def update_count(request, type):
    count = Count.objects.first()
    if count is not None:
        if request.method == "POST":
            if type == "like":
                count.like_count += 1
            elif type == "dislike":
                count.dislike_count += 1
            count.save()
            data1 = {
                "like_count" : count.like_count, 
                "dislike_count" : count.dislike_count
            }
            return render(request, "index.html", data1)
            # return JsonResponse(request, "index.html",data1)
            # return HttpResponse("Invalid response")
        else:
            return HttpResponse("Invalid response")

# def like_dislike(request):
#     count = Count.objects.first()

def homePage(request):
    data = {
    "title" : "home new",
    "bdata" : "Welcome to page 3",
    "clist" : ["django","java","python","flask"]
}
    return render(request, "index.html")
    # return JsonResponse(request, "index.html",data1)

# def aboutUs(request):
#     return HttpResponse("welcome to my world")

# def Course(request, courseid):
#     return HttpResponse(courseid)
