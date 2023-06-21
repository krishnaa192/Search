from django import forms

class FoodSearchForm(forms.Form):
    #query form field
    query = forms.CharField(label='Search Resturants by Name')

     