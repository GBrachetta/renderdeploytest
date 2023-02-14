from django.shortcuts import render


# Create your views here.
def index(request):
    """summary"""

    return render(request, "deployme/index.html", {})
