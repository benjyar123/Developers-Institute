from .models import Country, Category
import pycountry


def populate_categories():
    categories = ["Action", "Comedy", "Drama", "Romance", "Thriller", "Horror", "Documentary", "Science Fiction", "Animated"]
    for category in categories:
        Category.objects.get_or_create(name=category)


def countries():
    for country in pycountry.countries:
        Country.objects.get_or_create(name=country.name)
