from django.http import HttpResponseRedirect
from django.shortcuts import get_list_or_404, render
from .forms import SearchForm
from product.models import Product 

def home_page(request):

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SearchForm(request.POST)
        print("home page begin")
        # check whether it's valid:
        if form.is_valid(): 

            var_tmp = form.cleaned_data['main_search']
            #lst_product = get_list_or_404(Product, name__contains=var_tmp)
            lst_product = Product.objects.filter(name__contains = var_tmp)

            total = 0
            # Price range : échelle de prix
            # List product :   name, marque, description, prix_min, prix_max, 

            return render(request, 'home/resultat.html', {'lst_product': lst_product, 'total_results': total, 
                                                         
            'serach_form' :form})
        else:
            return render(request, 'home/thanks.html')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = SearchForm()

    return render(request, 'home/home.html', {'serach_form': form})


def thanks_page(request):
    return render(request, 'home/thanks.html')

def resultat_page(request):
    return render(request, 'resulat.html')


class ResultResearch:
    """
        All results of search. 
    """
    def __init__(self):
        self.price_min = 0
        self.price_max = 0
        self.name = "product name"
        self.description = "product description"
        self.brand = "product's brand"

