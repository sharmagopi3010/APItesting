import requests,json,jsonpath

url = "https://reqres.in/api/users?page=2"

response = requests.get(url)
res_json = json.loads(response.text)

for i in res_json['data']:
    assert i['first_name'] == 'Rachel'

assert response.status_code == 200


for i in res_json['data']:
    print(i['id'])

first_id = jsonpath.jsonpath(res_json,'data[0].id')
print(first_id)

for i in range (0, len(res_json)):
    all_ids = jsonpath.jsonpath(response.json(),'data['+str(i)+'].id')
    print (all_ids)


# assert response.status_code ==200

# json_response = json.loads(response.content)
# print(type(json_response))