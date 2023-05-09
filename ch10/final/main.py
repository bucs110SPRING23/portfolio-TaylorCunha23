import requests
import json

name = input("Enter a name:")

response_gender = requests.get(f"https://api.genderize.io/?name={name}").text
response_country= requests.get(f"https://api.nationalize.io/?name={name}").text


gender = json.loads(response_gender)['gender']
country = json.loads(response_country)['country']




print(f"{name} is most likely {gender} and {name}'s nationality is most likely {country}")

def __init__(self):
    self.url = "myapi.edu/"