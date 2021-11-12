# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(total_cash):
    return total_cash["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, cash):
    pet_shop ["admin"]["total_cash"] += cash


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
            



