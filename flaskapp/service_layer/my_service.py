import random
from data import the_office

def get_random_entry():
    return random.choice(the_office.the_office_people)
    

if __name__ == "__main__":
    print(get_random_entry())