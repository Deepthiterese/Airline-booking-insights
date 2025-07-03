import os
from amadeus import Client, ResponseError
from django.conf import settings

amadeus = Client(
    client_id=os.getenv("AMADEUS_API_KEY"),
    client_secret=os.getenv("AMADEUS_API_SECRET")
)

def get_real_prices(origin, destination, date, adults, max_results):
    try:
        response = amadeus.shopping.flight_offers_search.get(
            originLocationCode=origin,
            destinationLocationCode=destination,
            departureDate=date,
            adults=adults,
            max=max_results
        )
        prices = [round(float(offer['price']['total'])) for offer in response.data]
        return sorted(prices)
    except ResponseError as error:
        print("Amadeus API error:", error)
        return []

  

