## Source: https://pypi.org/project/requests/
## Docs: https://requests.readthedocs.io/en/latest/
## pip install requests
## 
## openweathermap.org - geolocation and weather APIs
## https://home.openweathermap.org/api_keys
## export OPEN_WEATHER_API_KEY=<enter_your_api_key>

# import requests module
import requests
# import os module
import os
# import json module
import json

# display all environment variables
# print("\nAll environment variables: ", os.environ)
# access an environment variable
print("\n HOME: ", os.environ['HOME'])
# access an environment variable
print("\n HOME: ", os.environ.get('1'))
# access an environment variable
print("\n HOME: ", os.getenv('USER'))

city_name = 'Mumbai' #'San Francisco'
state_code = 'MH' #'CA'
country_code = 'IN' #'US'
API_key = os.getenv('OPEN_WEATHER_API_KEY')

if API_key is None:
    print('API KEY is not available. Please check.')
else: 
    ## Use the GeoLocation API to get the latitude and longitude
    url = f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}'
    response = requests.get(url)
    try: 
        response.raise_for_status()
        response_json = json.loads(response.text)
        lat = response_json[0]['lat']
        lon = response_json[0]['lon']
        print('\n Latitude: ', lat)
        print('\n Longitude: ', lon)

        ## Use the weather API to get the temperature (in Celsius)
        url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={API_key}'
        response = requests.get(url)
        try: 
            response.raise_for_status()
            response_json = json.loads(response.text)
            print('\n Weather JSON: ', response_json)
            print('\n Weather: ', response_json['weather'])
            print('\n Weather main: ', response_json['weather'][0]['main'])
            print('\n Weather description: ', response_json['weather'][0]['description'])
            print('\n Main: ', response_json['main'])
            print('\n Main temp (Celsius): ', response_json['main']['temp'])
            print('\n Main feels like (Celsius): ', response_json['main']['feels_like'])
        except Exception as exc:
            print('Exception while accessing the Weather API: ', exc)

    except Exception as exc:
        print('Exception while accessing the GeoLocation API: ', exc)
