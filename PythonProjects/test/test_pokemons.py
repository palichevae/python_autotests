import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '25725a8da7db0dcd095f78da6a6b1986'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = 12834

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_trainer_name():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()['data'][0]['trainer_name'] == 'Елисей'

@pytest.mark.parametrize('key, value', [('trainer_name', 'Елисей'), ('id', '12834')])
def test_parametrize(key, value):
    response_parametrize = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_parametrize.json()['data'][0][key] == value