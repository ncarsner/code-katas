"""
GOAL: Create test environment users and passwords, utilizing a subtractive approach to array building by removing characters from a larger array, as opposed to the most common additive method.
"""
import string
import random
import json

min_pass_length = 12
max_pass_length = 64
number_of_users = 10

def password_generator():
    pw_values = string.printable.replace(string.whitespace,'') + ' '
    p = (random.choice(pw_values) for _ in range(random.randint(min_pass_length, max_pass_length)))
    return ''.join(p)

first_names = [ 'Alex','Blake','Chris','Dylan','Elliott','Flynn','Gene','Hunter','Ira','Jaime','Kelly','Lee','McKenzie','Nell','Owen','Peyton','Quinn','Reese','Sam','Taylor','Uri','Val','Wynn','Xi','Yordan','Zoe']

surnames = [ 'Adams','Allen','Anderson','Baker','Brown','Campbell','Carter','Clark','Davis','Flores','Garcia','Gonzalez','Green','Hall','Harris','Hernandez','Hill','Jackson','Johnson','Jones','King','Lee','Lewis','Lopez','Martin','Martinez','Miller','Mitchell','Moore','Nelson','Nguyen','Perez','Ramirez','Rivera','Roberts','Robinson','Sanchez','Scott','Taylor','Thomas','Thompson','Torres','Walker','White','Williams','Wilson','Wright','Young']

# CREATE USER LIST
new_users_needing_passwords = [(random.choice(first_names) + ' ' + random.choice(surnames).title()) for _ in range(number_of_users)]

new_users_passwords = [password_generator() for _ in range(number_of_users)]

# GENERATED AS LIST
def users_list():
    for i in range(len(new_users_needing_passwords)):
        user_id = ''.join([random.choice(string.digits) for _ in range(8)])
        user_short_name = new_users_needing_passwords[i].split()
        user_short_name = ''.join(user_short_name[0][0].lower() + user_short_name[1].lower())
        user_short_name = f'{user_short_name}{user_id}'
        user = new_users_needing_passwords[i]
        user_pass = new_users_passwords[i]
        spaces = len(max(new_users_needing_passwords, key=len))
        spacer = ' '
        print(f'[UID] {user_short_name} {spacer*(20-len(user_short_name))} [USER] {user} {spacer*(spaces-len(user))} [PASS] {user_pass}')

# GENERATED AS DICTIONARY
user_dict = dict(zip(new_users_needing_passwords, new_users_passwords))

if __name__ == '__main__':
    users_list()
    print('\n',json.dumps(user_dict, indent=4))