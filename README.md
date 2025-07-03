# ✈️ Airline Booking Demand Insights App

This Django web application visualizes market demand data for airline bookings using real-time APIs and web scraping.

---

## 🔧 Features

- ✅ Search flights using city names or IATA codes
- ✅ Auto-convert city names to IATA using Amadeus API
- ✅ Visualize price trends with interactive Chart.js graphs
- ✅ Scrape & show popular airline routes
- ✅ Clean, responsive UI styled with Bootstrap & custom CSS

---

## 📦 Setup Instructions

1. **Clone the repository**  
   ```bash
   git clone https://github.com/yourusername/airlineapp.git
   cd airlineapp

2. **Create a virtual environment**
      ```bash
    python -m venv env
    source env/bin/activate  # On Windows: env\Scripts\activate

3. **Install dependencies**
      ```bash
    pip install -r requirements.txt

4. **Add your API credentials**

Create a .env file in the root and add:
    
    AMADEUS_API_KEY=your_key
    AMADEUS_API_SECRET=your_secret

5.**Run the app**
   ```bash
    python manage.py runserver

6.**Visit**

    http://127.0.0.1:8000 
