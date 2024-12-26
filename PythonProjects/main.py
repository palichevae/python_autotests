import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '25725a8da7db0dcd095f78da6a6b1986'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_registration = {
    "trainer_token": TOKEN,
    "email": "palicheva.e@mail.ru",
    "password": "Palicheva2001)"
}
body_confirmation = {
    "trainer_token": TOKEN
}
body_pokemons_create = {
    "name": "Женек",
    "photo_id": 3
}
body_pokemons_change = {
    "pokemon_id": "172340",
    "name": "Ваушкин",
    "photo_id": 2
}
body_pokemons_add_pokeball = {
    "pokemon_id": "172340"
}

"""responce = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print (responce.text)"""

"""responce_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)
print (responce_confirmation.text)"""

responce_pokemons_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_pokemons_create)
print (responce_pokemons_create.text)

message = responce_pokemons_create.json()['message']
print (message)

responce_pokemons_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_pokemons_change)
print (responce_pokemons_change.text)

message = responce_pokemons_change.json()['message']
print (message)

responce_pokemons_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokemons_add_pokeball)
print (responce_pokemons_add_pokeball.text)

message = responce_pokemons_add_pokeball.json()['message']
print (message)