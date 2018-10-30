import requests
cardId = input("Please input card ID: ")

sensor = {
    "cardId" : cardId,
    "weight" : 50,
    "height" : 160,
}

r = requests.post('http://localhost:5000/scan', data = sensor)

# r = requests.get('http://localhost:5000')
# print(r.text)