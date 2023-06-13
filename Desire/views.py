from django.shortcuts import render

# Create your views here.

def homepage(request):
    Mtn = "+256 786822333"
    Airtel = "+256 752589677"
    context = {"Mtn":Mtn, "Airtel":Airtel}
    return render(request, "Desire/index.html", context)
