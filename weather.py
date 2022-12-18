import requests


def get_wether(s_city):
    city_id = 0
    appid = "152d754add9e83dd1d7f01c412744605"
    ourcity_weather = []
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/find",
                           params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': appid})
        data = res.json()
        cities = ["{} ({})".format(d['name'], d['sys']['country'])
                  for d in data['list']]
        ourcity_weather.append(cities)
        city_id = data['list'][0]['id']
    except Exception as e:
        print("Exception (find):", e)
        pass

    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                           params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
        data = res.json()
        ourcity_weather.append(data['weather'][0]['description'])
        ourcity_weather.append(data['main']['temp'])
    except Exception as e:
        print("Exception (weather):", e)
        pass

    return ourcity_weather
