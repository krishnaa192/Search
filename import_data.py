import csv
import os
import django
# Set up the environment for Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'search.settings')
django.setup()

from searchapp.models import Dish
# Open the file
with open('restaurants_small.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        resturant_name = row[1]  # Assuming the data name is in the 2nd column
        food=row[3] # Assuming the data name is in the 4th column
        dish = Dish(resturant_name=resturant_name,food=food)
        # Save the object into the database. You have to call save() explicitly.
        dish.save()
