import requests

EXPEDIA_API_URL = "https://example.com/expedia/api"

def search_hotels(destination, date, group_id=None):
    api_key = "YOUR_EXPEDIA_API_KEY"
    url = f"{EXPEDIA_API_URL}/hotels?destination={destination}&date={date}&apikey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        hotels = response.json()
        if group_id:
            discount = calculate_group_discount(group_id)
            for hotel in hotels:
                hotel["price"] *= (1.0 - discount)
        return hotels
    else:
        return []
