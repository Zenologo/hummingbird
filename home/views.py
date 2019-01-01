from django.http import HttpResponseRedirect
from django.shortcuts import get_list_or_404, render
from .forms import SearchForm
from product.models import Product 

def home_page(request):

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SearchForm(request.POST)
        # check whether it's valid:
        if form.is_valid(): 
            var_tmp = form.cleaned_data['main_search']
            lst_product = get_list_or_404(Product, name__contains=var_tmp)
            return render(request, 'home/resultat.html', {'lst_pro': lst_product})
        else:
            return render(request, 'home/thanks.html')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = SearchForm()

    return render(request, 'home/home.html', {'form': form})


def thanks_page(request):
    return render(request, 'home/thanks.html')

def resultat_page(request):
    return render(request, 'resulat.html')