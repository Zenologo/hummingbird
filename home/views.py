from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import SearchForm


def home_page(request):

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SearchForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('thanks.html')
            
    # if a GET (or any other method) we'll create a blank form
    else:
        form = SearchForm()

    return render(request, 'home/home.html', {'form': form})


def thanks_page(request):
    return render(request, 'home/thanks.html')