from django.shortcuts import render

# Create your views here.

def home_page(request):
    """A view of all bands."""
    # bands = models.Band.objects.all()
    return render(request, 'home/home.html')