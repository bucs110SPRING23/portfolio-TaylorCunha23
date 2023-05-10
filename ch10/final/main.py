import requests
import json

class Genderize:
    def __init__(self):
        self.url = "https://api.genderize.io"

    def get_gender(self, name):
        url = f"{self.url}?name={name}"
        response = requests.get(url)
        gender_data = response.json()
        if 'gender' in gender_data:
            return gender_data['gender']
        else:
            return None


class Nationalize:
    def __init__(self):
        self.url = "https://api.nationalize.io"

    def get_nationality(self, name):
        url = f"{self.url}?name={name}"
        response = requests.get(url)
        nationality_data = response.json()
        if 'country' in nationality_data:
            countries = nationality_data['country']
            if len(countries) > 0:
                nationality_info = countries[0]
                if 'country_id' in nationality_info:
                    return nationality_info['country_id']
        return None


class NameAnalyzer:
    def __init__(self):
        self.gender_api = Genderize()
        self.nationality_api = Nationalize()

    def analyze_name(self, name):
        gender = self.gender_api.get_gender(name)
        nationality = self.nationality_api.get_nationality(name)

        return gender, nationality

    def __str__(self):
        return "NameAnalyzer"

def main():
    print("Welcome to the name gender and nationality generator. Input a name and find out what gender most individuals with that name are and their nationality.")
    name = input("Enter a name: ")
    analyzer = NameAnalyzer()
    gender, nationality = analyzer.analyze_name(name)
    
    if gender and nationality:
        print(f"The name {name} is most likely {gender} and from {nationality}. Please note that {nationality} is a country code.")
    else:
        print(f"Could not determine the gender and/or nationality for the name {name}.")

if __name__ == "__main__":
    main()

