# WRITE YOUR FUNCTIONS HERE

######################################
#                   MVP              #
######################################
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]


def get_total_cash(total_cash):
    return total_cash["admin"]["total_cash"]


def add_or_remove_cash(pet_shop, cash):
    pet_shop["admin"]["total_cash"] += cash


def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]


def increase_pets_sold(pet_shop, sold):
    pet_shop["admin"]["pets_sold"] += sold


def get_stock_count(pet_shop):
    return len(pet_shop["pets"])


def get_pets_by_breed(pet_shop, breed):
    no_of_pets_by_breed = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            no_of_pets_by_breed.append(pet["name"])
    return no_of_pets_by_breed


def find_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            return pet
    return None


def remove_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            pet_shop["pets"].remove(pet)


def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)


def get_customer_cash(customer):
    return customer["cash"]


def remove_customer_cash(customer, to_remove):
    customer["cash"] -= to_remove


def get_customer_pet_count(customer):
    count = customer["pets"].copy()
    return len(count)


def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)



#############################################
#              extension 1                  #
#############################################

def customer_can_afford_pet(customer, new_pet):
    return customer["cash"] >= new_pet["price"]


#############################################
#              extension 2                  #
#############################################

def sell_pet_to_customer(pet_shop, pet, customer):
    if pet == None: #checking if pet exists
        return
    elif customer_can_afford_pet(customer, pet) == False:   #checking if can afford
        return
    else:
        add_pet_to_customer(customer, pet)
        price = pet["price"] # getting price to pass into removing customer cash and adding cash to shop
        remove_customer_cash(customer, price)
        add_or_remove_cash(pet_shop, price)
        pet_name = pet["name"]
        remove_pet_by_name(pet_shop, pet_name)
        sold = 1
        increase_pets_sold(pet_shop, sold)