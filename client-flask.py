import requests

#r=requests.get('http://127.0.0.1:5000/api/v1/comptes_telephoniques')
#data=r.json()
#for item in data["tasks"]:
#    print(f"Title: {item.get('title')}")
#    print(f"Description: {item.get('description')}")
 #   print("########################################")

a=int(input("saisir un nombre:"))
b=int(input("saisir un autre nombre:"))
r=requests.get('http://172.0.0.1:5000/sold/{a}/{b}')
data=r.json()
print(f"le somme de {a} et {b}={data['somme']}")

def get_phones():
    response = requests.get('http://127.0.0.1:5000/phones')
    return response.json()

def get_phone_by_id(phone_id):
    response = requests.get('http://127.0.0.1:5000/phones/{}'.format(phone_id))
    return response.json()

def add_phone(phone):
    response = requests.post('http://127.0.0.1:5000/phones', json=phone)
    return response.json()

def update_phone(phone_id, phone):
    response = requests.put('http://127.0.0.1:5000/phones/{}'.format(phone_id), json=phone)
    return response.json()

def delete_phone(phone_id):
    requests.delete('http://127.0.0.1:50005000/phones/{}'.format(phone_id))
    return True

# Usage
inventory = get_phones()
print(inventory)

new_phone = {
    'phone_id': '123',
    'model': 'iPhone 12',
    'quantity': 10
}
added_phone = add_phone(new_phone)
print(added_phone)

phone_to_update = {
    'quantity': 12
}
updated_phone = update_phone(added_phone['phone_id'], phone_to_update)
print(updated_phone)

deleted_phone = delete_phone(updated_phone['phone_id'])
print(deleted_phone)



    