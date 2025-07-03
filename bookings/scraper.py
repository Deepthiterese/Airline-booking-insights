import requests
from bs4 import BeautifulSoup

def scrape_popular_routes():
    url = "https://en.wikipedia.org/wiki/List_of_busiest_passenger_air_routes"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Locate the main table
        table = soup.find("table", class_="wikitable")
        routes = []

        if table:
            rows = table.select("tr")[1:11]  # Top 10 rows after header

            for row in rows:
                cols = row.find_all("td")
                if len(cols) >= 3:
                    origin = cols[1].get_text(strip=True)
                    destination = cols[2].get_text(strip=True)
                    route = f"{origin} to {destination}"
                    routes.append(route)

        return routes if routes else fallback_routes()

    except Exception as e:
        print("Wikipedia scraping failed:", e)
        return fallback_routes()

def fallback_routes():
    return [
        "New York to London",
        "Los Angeles to Tokyo",
        "Delhi to Dubai",
        "Paris to Rome",
        "Singapore to Sydney",
        "Mumbai to Bangkok",
        "Toronto to Vancouver",
        "Chicago to Frankfurt",
        "San Francisco to Hong Kong",
        "Istanbul to Amsterdam"
    ]
