import requests

#Aries, Taurus, Gemini, Cancer, Leo, Virgo, Libra, Scorpio, Sagittarius, Capricorn, Aquarius, Pisces

sign = input("Enter your zodiac sign:")

day = input("Enter the horoscope day (today, tomorrow, or yesterday)")

params = (

    ('sign', sign),
    ('day', day)

)

response = requests.post('https://aztro.sameerkumar.website/', params=params)

print(response.json())

# def main():
#     pygame.init()
#     # Create an instance on your controller object
#     # Call your mainloop

#     ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######


# # https://codefather.tech/blog/if-name-main-python/
# if __name__ == "__main__":
#     main()

