from django import forms

class SearchForm(forms.Form):
    main_search = forms.CharField(label='',  
            widget = forms.TextInput(attrs={'placeholder': 'Rechercher un produit ou suivir un colis', 'size':'40'}), 
            max_length=100)