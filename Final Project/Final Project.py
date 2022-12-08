# This program takes data from the Plant Catalog and displays each
# plant's common name, botanical name, zone, light, and price. The item
# count of the catalog and the average price of the items in the catalog
# will be displayed.

# References:
# https://docs.python.org/3/library/stdtypes.html#str.startswith
# https://stackoverflow.com/questions/67528351/how-to-loop-on-startswith-method
# https://blog.finxter.com/how-to-convert-a-string-list-to-a-float-list-in-python/
# https://stackoverflow.com/questions/2507808/how-to-check-whether-a-file-is-empty-or-not

import os


def main():
    plant_catalog = 'plant_catalog.xml'
    if os.path.isfile(plant_catalog):
        tag = 'COMMON' or 'BOTANICAL' or 'ZONE' or 'LIGHT' or 'PRICE'
        empty_file_check(plant_catalog)
        common_names = process_lists(plant_catalog, 'COMMON')
        botanical_names = process_lists(plant_catalog, 'BOTANICAL')
        growing_zones = process_lists(plant_catalog, 'ZONE')
        light_levels = process_lists(plant_catalog, 'LIGHT')
        plant_price = process_lists(plant_catalog, 'PRICE')
        display_catalog(common_names, botanical_names,
                      growing_zones, light_levels, plant_price)
        average_price = calculate_average(plant_price)
        display_statistics(average_price, plant_price)
    else:
        print("File does not exist")
        
        
def empty_file_check(plant_catalog):
    if os.stat(plant_catalog).st_size == 0:
        print("File is empty")
        
        
def process_lists(plant_catalog, tag):
    array = []
    with open(plant_catalog, 'r') as file_contents:
        for line in file_contents:
            line = line.strip()
            line = line.replace('<', '').replace('>', '').replace('/', '')
            line = line.replace('$', '')
            if any([line.startswith(tag)]):
                try:
                    line = line.removeprefix(tag).removesuffix(tag)
                    array.append(line)
                except:
                    pass
        if len(array) == 0:
            print('Error: Missing or bad data')
    return array


def display_catalog(common_names, botanical_names, growing_zones,
                  light_levels, plant_price):
    for index in range(len(common_names)):
        print(str(common_names[index]) + 
              ' (' + str(botanical_names[index]) + ') ' +
              ' - ' + str(growing_zones[index]) + ' - ' +
              str(light_levels[index]) + ' - $' + str(plant_price[index]))


def calculate_average(plant_price):
    plant_price = [float(price) for price in plant_price]
    total = sum(plant_price)
    average_price = round(total / (len(plant_price)), 2)
    return average_price


def display_statistics(average_price, plant_price):
    print(str(len(plant_price)) + ' items - $' +
          str(average_price) + ' average price.')
    
    
main()     
