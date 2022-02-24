"""
Lab 3 Task 2
"""
class Markets:
    """
    class Markets
    """
    def __init__(self, name, area, categories):
        """
        names of values
        >>> market_family_food = Markets('Family Food', 80, ['Bread and Bakery', 'Dairy',\
'Beverages'])
        >>> market_family_food.name
        'Family Food'
        """
        self.name = name
        self.area = area
        self.categories = categories

    def __str__(self):
        """
        returns an information about the supermarket
        >>> market_family_food = Markets('Family Food', 80, ['Bread and Bakery', 'Dairy',\
'Beverages'])
        >>> str(market_family_food)
        'Supermarket Family Food has an area of 80m2 and has the folowinf categories: Bread\
 and Bakery, Dairy, Beverages.'
        """
        categ = ''
        for cat in self.categories:
            categ += cat + ', '
        return f'Supermarket {self.name} has an area of {self.area}\
m2 and has the folowinf categories: {categ[:-2]}.'
