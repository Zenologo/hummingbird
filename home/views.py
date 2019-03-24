from django.http import HttpResponseRedirect
from django.shortcuts import get_list_or_404, render
from .forms import SearchForm
#from product.models import Product
from merchant.models import PriceMonitor, MerchantProduct

def home_page(request):

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SearchForm(request.POST)
        print("home page begin")
        # check whether it's valid:
        if form.is_valid(): 

            var_tmp = form.cleaned_data['main_search']
            #lst_product = get_list_or_404(Product, name__contains=var_tmp)
            # lst_product = Product.objects.filter(name__contains = var_tmp)

            lst_product = PriceMonitor.objects.filter(merchant_product__product__name__contains = var_tmp)

            total = len(lst_product)
            print("Total: " + str(total))
            
            set_name = set()
            lst_items = []
            for item in lst_product:
                if item.merchant_product not in set_name:
                    """ Create a new item in result list"""
                    set_name.add(item.merchant_product)
                    item_prod = ItemSearch()
                    item_prod.name = item.merchant_product.product.name
                    item_prod.brand = item.merchant_product.brand
                    item_prod.description = item.description

                    item_prod.price_max = item.price
                    item_prod.price_min = item.price

                    item_prod.url = "http://127.0.0.1"
                    lst_items.append(item_prod)
                else:
                    for price_item in lst_items:
                        """ Update price range """
                        if price_item.name == item.merchant_product:
                            if price_item.price_max < item.price:
                                price_item.price_max = item.price
                            elif price_item.price > item.price:
                                price_item.price = item.price
                            break
                            
            return render(request, 'home/resultat.html', {'lst_product': lst_items, 
                                                            'total_results': total,                         
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


class ItemSearch:
    """
        All results of search page.
    """
    def __init__(self):
        self.price_min = 0
        self.price_max = 0
        self.name = "product name"
        self.description = "product description"
        self.brand = "product's brand"
        self.url = "http://127.0.0.1"

