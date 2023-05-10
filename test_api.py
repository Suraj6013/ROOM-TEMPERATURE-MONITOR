import requests

# api_url = input('Enter API URL: ')

response = requests.get("http://192.168.213.36")

#print(response)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f'Request failed with status code {response.status_code}')

