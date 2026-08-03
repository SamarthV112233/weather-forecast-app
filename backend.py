import requests

API_KEY = "4320a22c738ae2ee1e3c58132bccb393"


def get_data(place, forecast_days=None, condition=None):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data


if __name__ == "__main__":
    print(get_data(place="Tokyo"))