import requests

SKYSCANNER_API_URL = "https://partners.api.skyscanner.net/apiservices/browsequotes/v1.0/US/USD/en-US"

def search_flights(origin, destination, date, group_id=None):
    api_key = "YOUR_SKYSCANNER_API_KEY"
    url = f"{SKYSCANNER_API_URL}/{origin}-sky/{destination}-sky/{date}?apikey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        flights = response.json()["Quotes"]
        if group_id:
            discount = calculate_group_discount(group_id)
            for flight in flights:
                flight["MinPrice"] *= (1.0 - discount)
        return flights
    else:
        return []
