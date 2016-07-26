import csv


def main():
    FILENAME = "SacramentoResidentialRealEstateTransactions2008.csv"
    printHeader()
    while True:
        try:
            # ask the user what they want to do
            choice = menu()

            #[L]oad data file
            if choice == "L":
                readData(FILENAME)

            # [C]ondo prices
            if choice == "C":
                print(average_price_condo(reader))

            # [A]verage price of all properties
            if choice == "A":
                print(average_price(reader))

            # [P] find hi/lo priced
            if choice == "P":
                hiLow = find_high_and_low(reader)
                print("%20s %-10s %20s %-10s " %("\nMost Expensive Property:", hiLow[0], "\nLeast Expensive Property:", hiLow[1]))

            # [Q]uit
            elif choice == "Q":
                print("ok bye")
                break

        except NameError :
            print("Error: You must load the file before any data can be analyzed")


def average_price(reader):
    price = get_average_price(reader, "price")
    beds = get_average_price(reader, "beds")
    baths = get_average_price(reader, "baths")
    return "%-35s %10s %-35s %10s %-35s %10s" % ("\nAverage Price:", "$"+str(price), "\nAverage Number of Bedrooms:", beds,\
                                                "\nAverage Number of Bathrooms:", baths)


def get_average_price(reader, colunm):
    total = 0
    counter = 0
    for row in reader:
        total += int(row[colunm])
        counter += 1
    return total // counter



def average_price_condo(reader):
    condos_reader = list(reader)
    for row in condos_reader:
        if row["home_type"] != "Condo":
            condos_reader.remove(row)
    return average_price(condos_reader)


def readData(filename):
    data_file = open(filename, "r")
    reader = list(csv.DictReader(data_file))
    return reader


def find_high_and_low(reader):
    max = 0
    min = 100000
    for row in reader:
        if int(row["price"]) > max:
            max = int(row["price"])
    for row in reader:
        if int(row["price"]) < min:
            min = int(row["price"])
    return max, min

def menu():
    userInput = " "
    while userInput not in "LPACQ":
        userInput = input(
            "\n\nSelect an Action: \n[L]oad data file \n[P] find hi/lo priced \n[A]verage all properties \n[C]ondo averages: \n[Q]uit\n")
        userInput = userInput.upper()
    return userInput


def printHeader():
    print("Sacramento Real Estate Data Processor v1.0")


main()
