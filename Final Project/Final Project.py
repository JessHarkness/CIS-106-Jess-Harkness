# This program takes data from the Plant Catalog and displays each
# plant's common name, botanical name, zone, light, and price. The item
# count of the catalog and the average price of the items in the catalog
# will be displayed.

# References: https://docs.python.org/3/library/stdtypes.html#str.startswith
# References: https://stackoverflow.com/questions/67528351/how-to-loop-on-startswith-method

import os
def main():
    plant_catalog = '/Users/jessharkness/Desktop/CIS 106/plant_catalog.xml'
    if os.path.isfile(plant_catalog):
        common_names = process_lists(plant_catalog, 'COMMON')
        botanical_names = process_lists(plant_catalog, 'BOTANICAL')
        growing_zones = process_lists(plant_catalog, 'ZONE')
        light_levels = process_lists(plant_catalog, 'LIGHT')
        plant_prices = process_lists(plant_catalog, 'PRICE')
        display_catalog(common_names, botanical_names,
                      growing_zones, light_levels, plant_prices)
        average_price = calculate_average(plant_prices)
        display_statistics(average_price, plant_prices)
    else:
        print("File does not exist.")
        
def process_lists(plant_catalog):
    common_names = []
    botanical_names = []
    growing_zones = []
    light_levels = []
    plant_prices = []
    with open(plant_catalog, 'r') as file_contents:
    for line in file_contents:
        line = line.strip()
        if any([line.startswith('<COMMON>')]):
            common_name = line.removeprefix('<COMMON>').removesuffix('</COMMON>')
            common_names.append(common_name)
# repeat this function for each variable (botanical, light, zone, price)
# for prices list, list data type will be changed to float
# only one function is needed for processing lists, and this function
# will be called five times (once for each list)
        
def display_items(common_names, botanical_names, growing_zones,
                  light_levels, plant_prices):
    for index in range(len(common_names)):
    print(str(common_names[index]) + ' (' +str(botanical_names[index]) + ') ' + ' - ' + str(growing_zones[index]) + ' - ' + str(light_levels[index]) + ' - $' + str(plant_prices[index]))

def calculate_average(plant_prices):
    total = sum(plant_prices)
    average_price = round(total / (len(plant_prices)), 2)
    return average_price

def display_statistics(average_price, plant_prices):
    print(str(len(plant_prices)) + ' items. - $' + str(average_price) + ' average price.')
 
          