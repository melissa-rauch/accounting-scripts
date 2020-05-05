"""Print out all the melons in our inventory."""

#import melon.py
from melons import melons


def print_melons(melons):
    """Print each melon with corresponding attribute information."""
    #For Melon (Keys) names in Dictionary, print the Melon name sin uppercase
    for melon_names, attributes in melons.items():
        print(melon_names.upper())
        # For the various Values in attributes in Melon dictionary
        #Print attribut:Value
        for attribute, value in attributes.items():
            print(f"{attribute}: {value}")
#Call Function
print_melons(melons) 