from django.shortcuts import render
from datetime import datetime, timedelta
from .aviation_api import get_real_prices
from .scraper import scrape_popular_routes

def home(request):
    # Set today's date for default
    today_str = datetime.today().strftime('%Y-%m-%d')

    # Extract form data or fallback to defaults
    source = request.GET.get("source", "")
    destination = request.GET.get("destination", "")
    date = request.GET.get("date", today_str)
    adults = int(request.GET.get("adults", 1))
    max_results = int(request.GET.get("max", 5))

    data = {
        "source": source,
        "destination": destination,
        "date": date,
        "adults": adults,
        "max": max_results,
        "today": today_str  # for setting `min` in <input type="date">
    }

    # Only fetch results if both source and destination are provided
    if source and destination:
        source = source.upper()
        destination = destination.upper()

        prices = get_real_prices(source, destination, date, adults, max_results)
        departure_date = datetime.strptime(date, '%Y-%m-%d')
        trends = [(departure_date + timedelta(days=i)).strftime('%d %b %Y') for i in range(len(prices))]
        routes = scrape_popular_routes()

        data.update({
            "prices": prices,
            "trends": trends,
            "routes": routes,
        })

    return render(request, 'bookings/home.html', data)
