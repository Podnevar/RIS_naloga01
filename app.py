artikli = []

def input_of_articles():
    ime = raw_input("Ime izdelka: ")
    cena = raw_input("Cena izdelka: ")
    zaloga = raw_input("Zaloga izdelka: ")
    dobavitelj = raw_input("dobavitelj izdelka: ")

    artikel = {"ime": ime,
        "cena": cena,
        "zaloga": zaloga,
        "dobavitelj": dobavitelj}

    return artikel

def read_products():
    file = open("artikli.txt","r")
    lines = file.read().split(";")
    lines.pop(-1)

    for line in lines:
        productProperties = line.split(",")
        product = {"ime": productProperties[0],
                   "cena": productProperties[1],
                   "zaloga": productProperties[2],
                   "dobavitelj": productProperties[3]}
        artikli.append(product)

    return artikli

def print_all_products():
    for product in read_products():
        print('{},{},{},{};'.format(product["ime"], product["cena"], product["zaloga"], product["dobavitelj"]))

def write_products():
    continueLoop = "DA"
    while continueLoop == "DA":
        artikel = input_of_articles()
        artikli.append(artikel)
        print("Izdelek je bil dodan!")
        continueLoop = raw_input("Ce zelite nadaljevati vnesite DA: ")

    file = open("artikli.txt", "w+")

    for artikel in artikli:
        file.write('{},{},{},{};'.format(artikel["ime"], artikel["cena"], artikel["zaloga"], artikel["dobavitelj"]))
    file.close()


def find_product_by_supplier_and_price():
    supplier = raw_input("Vnesite naziv dobavitelja: ")
    price = int(raw_input("Vnesite iskano ceno"))
    allProducts = read_products()
    #poiscemo produkt ki ima ceno manjso od iskane in istega dobavitelja
    foundProducts = (x for x in allProducts if int(x["cena"]) < price and x["dobavitelj"]==supplier)

    file = open("iskani_artikli.txt", "w+")

    for product in foundProducts:
        print('{},{},{},{};'.format(product["ime"], product["cena"], product["zaloga"], product["dobavitelj"]))
        file.write('{},{},{},{};'.format(product["ime"], product["cena"], product["zaloga"], product["dobavitelj"]))

    file.close()


def reduce_product_price():
    name = raw_input("Vnesite ime produkta: ")
    discount = raw_input("Vnesite znizanje (npr. 0.10 za 10%): ")
    allProducts = read_products()
    #izberemo prvi produkt, ki ustreza pogoju
    foundProduct = next(x for x in allProducts if x["ime"]==name)

    #izracunamo popust
    currentPrice=int(foundProduct["cena"])
    newPrice = currentPrice - (currentPrice*float(discount))

    foundProduct["cena"]=newPrice
    #znizan artikel zapisemo v nov dokument
    file = open("akcija.txt", "w+")
    file.write('{},{},{},{};'.format(foundProduct["ime"], foundProduct["cena"], foundProduct["zaloga"], foundProduct["dobavitelj"]))
    file.close()

#USER INTERFACE


while 1==1:
    optionNum = int(raw_input(
        "Vnesite 1 za dodajanje artiklov, 2 za izpis vseh artiklov ali iskanje po dobavitelju in ceni, 3 za popuste: "))
    if(optionNum==1):
        write_products()
    elif(optionNum==2):
        optionNum = int(raw_input("Vnesite 1 za izpis vseh artiklov, 2 za iskanje po dobavitelju in ceni"))

        if optionNum==1:
            print_all_products()
        elif optionNum==2:
            find_product_by_supplier_and_price()
        else:
            print("Napaka pri vnosu")
    elif(optionNum==3):
        reduce_product_price()