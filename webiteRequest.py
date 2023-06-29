import requests

response = requests.get('https://www.example.com')

# print the status code
print(response.status_code)

# print the content of the response
print(response.text)
