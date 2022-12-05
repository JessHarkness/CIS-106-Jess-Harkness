# This program takes data from the Plant Catalog and displays each
# plant's common name, botanical name, zone, light, and price. The item
# count of the catalog and the average price of the items in the catalog
# will be displayed.

import os
def main():
    plant_catalog = '/Users/jessharkness/Desktop/CIS 106/plant_catalog.xml'
    if os.path.isfile(plant_catalog):
        common_names_list = process_lists(plant_catalog, 'COMMON')
        botanical_names_list = process_lists(plant_catalog, 'BOTANICAL')
        growing_zones_list = process_lists(plant_catalog, 'ZONE')
        light_levels_list = process_lists(plant_catalog, 'LIGHT')
        plant_prices_list = process_lists(plant_catalog, 'PRICE')
        display_catalog(common_names, botanical_names,
                      growing_zones, light_levels, plant_prices)
        average_price = calculate_average(plant_prices)
        display_statistics(average_price, plant_prices)
        
def process_lists(plant_catalog):
    common_names_list = []
    botanical_names_list = []
    growing_zones_list = []
    light_levels_list = []
    plant_prices_list = []
    with open(plant_catalog, 'r') as file_contents:
        
    

                