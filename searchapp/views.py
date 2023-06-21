from django.shortcuts import render
from searchapp.forms import *
from searchapp.models import *
# Create your views here.


#view for search page 
def search_dishes(request):
    # if this is a POST request we need to process the form data
    form = FoodSearchForm(request.GET)
    # create a form instance and populate it with data from the request:
    if form.is_valid():
        # process the data in form.cleaned_data as required
        query = form.cleaned_data['query']
        dishes = Dish.objects.filter(resturant_name__icontains=query)
        #
    else:
        # if a GET (or any other method) we'll create a blank form
        dishes = Dish.objects.none()
    
    return render(request, 'search.html', {'form': form, 'dishes': dishes})
