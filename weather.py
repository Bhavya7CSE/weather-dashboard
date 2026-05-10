import requests
API_KEY= "04ffa43c5d241607d1dd7e02d9212d7d"
while True:
    city=input("\nEnter City name(or exit to quit):")
    if city.lower()=="exit":
        break
    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={YOUR API KEY}&units=metric"
    try:
        response=requests.get(url)
        data=response.json()
        if data["cod"]!=200:
            print("City not found.Try again.") 
            continue
        temp=data["main"]["temp"]
        weather=data["weather"][0]["description"]
        humidity=data["main"]["humidity"]
        wind=data["wind"]["speed"]
        print(f"\n Weather in {city}")
        print(f"\n Temperature:{temp}*c")
        print(f"condition:{weather}")
        print(f"humidity:{humidity}%")
        print(f"wind speed:{wind}m/s")
    except:
        print("Network error.Check ur internet")                 