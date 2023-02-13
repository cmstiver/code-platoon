import csv


def find_pet():

    while (True):
        try:
            pet_type = input(
                "What type of pets are you looking for?: ").lower()
            csv_file = open(f"./data/{pet_type}.csv")
            break
        except:
            print(
                f'Sorry, we don\'t have any {pet_type} here.')

    csv_list = list(csv.DictReader(csv_file, skipinitialspace=True))

    isNotDone = True
    while (isNotDone):
        pet_name = input("What is the pet's name?: ").lower()
        for pet in csv_list:
            if pet['name'] == pet_name:
                isNotDone = False
                return f"{pet['name']} is a {pet['age']} year old {pet['breed']}."
            else:
                print(
                    f'Sorry, we don\'t have a {pet_name} here.')
                break

    csv_file.close()

    pass


print(find_pet())
