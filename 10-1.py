pets ={}

def input_pet(pet):
    name = input("имя питомца:")
    type = input("тип питомца:")
    age = int(input("возраст питомца:"))
    owner = input("владелец питомца:")
    pet[name] = {}
    pet[name]['тип питомца']= type
    pet[name]['возраст']= age
    pet[name]['владелец']= owner
    return pet
pet = {}
pet = input_pet(pet)
print(pet)
pet = input_pet(pet)
print(pet)
