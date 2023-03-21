import json
from csv import DictReader

new_users_json = dict()
new_users_list = []

with open('users.json', 'r') as users:
    users_json = json.load(users)

for user in users_json:
    intermediate_list_for_json = {}
    new_users_json['name'] = user.get('name')
    new_users_json['gender'] = user.get('gender')
    new_users_json['address'] = user.get('address')
    new_users_json['age'] = user.get('age')
    new_users_json['books'] = []
    intermediate_list_for_json = dict(new_users_json)
    new_users_list.append(intermediate_list_for_json)


def user_generate():
    for polsovatel in new_users_list:
        yield polsovatel


generator_of_users = user_generate()

new_book = dict()
new_book_list = []

with open('books.csv', newline='') as library:
    books = DictReader(library)

    for book in books:
        intermediate_list_for_csv = dict()
        new_book['title'] = book.get('Title')
        new_book['author'] = book.get('Author')
        new_book['pages'] = book.get('Pages')
        new_book['genre'] = book.get('Genre')
        intermediate_list_for_csv = dict(new_book)
        iter_user = iter(generator_of_users)
        next_user = next(iter_user, 'stop')
        if next_user == 'stop':
            generator_of_users = user_generate()
            iter_user = iter(generator_of_users)
            next_user = next(iter_user, 'stop')
            next_user['books'].append(intermediate_list_for_csv)
        else:
            next_user['books'].append(intermediate_list_for_csv)

            with open('result.json', 'w') as file:
                json.dump(new_users_list, file, indent=4)
