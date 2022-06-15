import requests

API_KEY = "70e123743c7a3e7c0a7651557252e843"


print("Hello and welcome to the weather APP ")
print("Type number 1 if you want to search by city")
print("Type number 2 if you want to search by coordinates")

def extraxt_response(response, unit):
    if response.status_code == 200:
        data = response.json()
        weather = data["weather"]
        for i in weather:                
            temp = data["main"]["temp"]
            description = i["description"]
            if unit == "c":
                print("Feels like " + str(int(temp)) + "°C,", description)
            else:
                print("Feels like " + str(int(temp)) + "°F,", description)
    else:
        print("Bad request")
        
while True:
    answer = input("Choose 1/2? ")
    if answer.isdigit():
        if int(answer) == 1:
            while True:
                unit = input("Do you want the unit in celsius or in fahrenheit? choose c/f: ").lower()
                if unit in ["c", "f"]:
                    if unit == "c":
                        city = input("Please type your city: ")
                        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric")
                        extraxt_response(response, unit)
                        break
                    elif unit == "f":
                        city = input("Please type your city: ")
                        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=imperial")
                        extraxt_response(response, unit)
                        break
        elif int(answer) == 2:
            lat = input("Please type your latitude: ")
            lon = input("Please type your longitude: ")
            while True:
                unit = input("Do you want the unit in celsius or in fahrenheit? choose c/f: ").lower()
                if unit in ["c", "f"]:
                    if unit == "c":
                        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric")
                        extraxt_response(response, unit)
                        break
                    elif unit == "f":
                        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=imperial")
                        extraxt_response(response, unit)
                        break
            break
        
