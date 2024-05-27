import csv
from datetime import datetime

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.
    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """

    dictionary = {}
    header = []
    try:
        with open(filename, "r") as csv_file:
            reader = csv.reader(csv_file)
            header = next(reader)
            key = header.index(key_column_index)
            for data in reader:
                dictionary[data[key]] = data
    
        return dictionary
    except  PermissionError as perm_err:
        print(perm_err)
    except FileNotFoundError as not_found_err:
        print(not_found_err)
    except KeyError as key_err:
        print(type(key_err).__name__, key_err)
 

def make_receipt(dict, filename):
    today = datetime.now()
    
    print("Machado´s Store")

    number_of_item = 0
    subtotal = 0
    try:
        with open(filename, "r") as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            for row in reader:
                number_of_item = int(row[1]) + number_of_item
                subtotal = (float(dict[row[0]][2])*int(row[1])) + subtotal
                print(f"{dict[row[0]][1]}: {row[1]} @ {dict[row[0]][2]}")
    except  PermissionError as perm_err:
        print(perm_err)
    except FileNotFoundError as not_found_err:
        print(not_found_err)
    except KeyError as key_err:
        print(type(key_err).__name__, key_err)
    
    sales_tax = subtotal*0.06
    discount = get_discount(today, subtotal)

    print(f"Number of Items: {number_of_item}")
    print(f"Subtotal: {subtotal}")
    print(f"Sales Tax: {sales_tax}")
    if discount != 0:
        subtotal = discount
        print(f"Discount: {subtotal - discount}")
    print(f"Total: {subtotal+sales_tax}")
    print("Thank you for shopping at the Machado´s Store.")
    print(f"{today.strftime("%c")}")

def get_discount(day, value):
    if(day.strftime("%w") == 2 or day.strftime("%w") == 3 or day.strftime("%H") < 11):
        value = value - (value*0.1)
    return value

def main():
    products_dict = read_dictionary("week5/grocery_store/products.csv", "Product #")
    if products_dict != None:
        make_receipt(products_dict, "week5/grocery_store/request.csv")

if __name__ == "__main__":
    main()