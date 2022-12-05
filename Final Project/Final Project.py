# This program takes data from the Plant Catalog and displays each
# plant's common name, botanical name, zone, light, and price. The item
# count of the catalog and the average price of the items in the catalog
# will be displayed.

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
        print("File name is invalid or file does not exist.")
        
def process_lists(plant_catalog):
    common_names_list = []
    botanical_names_list = []
    growing_zones_list = []
    light_levels_list = []
    plant_prices_list = []
    with open(plant_catalog, 'r') as file_contents:
        # conditional statements? if common name, add to common list. if botanical name,
        # add to botanical list, etc.
        # append according list
        # for prices list, list type will be changed to integer
        # only one function is needed for processing lists, and this function
        # will be called five times (once for each list)
        
def display_items(common_names, botanical_names, growing_zones,
                  light_levels, plant_prices):
    for index in range(len(common_names)):
        print(common_names[index] + ' ('+ botanical_names[index] + ')' + ' - ' + growing_zones[index] + ' - ' + light_levels[index] + ' - ' + plant_prices[index])

def calculate_average(plant_prices):
    total = sum(plant_prices)
    average_price = round(total / (len(plant_prices)), 2)
    return average_price

def display_statistics(average_price, prices_list):
    print((len(prices_list)) + ' items. - $' + average_price + ' average price.') 
          