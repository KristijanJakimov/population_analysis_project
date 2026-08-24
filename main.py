from helpers import fetch_page, save_to_csv
from countries_scraper import scrape_countries
from regions_scraper import scrape_region
from history_scraper import scrape_history

BASE_URL = "https://www.worldometers.info"
COUNTRIES_URL = "https://www.worldometers.info/world-population/population-by-country/"
COUNTRY_FIELDS = ["rank", "country", "url", "population", "yearly_change", "net_change","density", "land_area", "migrants", "fertility_rate", "median_age", "urban_pop", "world_share"]

html = fetch_page(COUNTRIES_URL)
countries = scrape_countries(html)
save_to_csv(countries, "countries.csv", COUNTRY_FIELDS)

REGION_URLS={"Africa": "https://www.worldometers.info/population/africa/","Asia": "https://www.worldometers.info/population/asia/",
"Europe": "https://www.worldometers.info/population/europe/","Latin America and the Caribbean": "https://www.worldometers.info/population/latin-america-and-the-caribbean/",
"Northern America": "https://www.worldometers.info/population/northern-america/","Oceania": "https://www.worldometers.info/population/oceania/",}

REGION_FIELDS = ["country", "continent"]

regions = []
for continent, url in REGION_URLS.items():
    region_html = fetch_page(url)
    regions.extend(scrape_region(region_html, continent))
save_to_csv(regions, "regions.csv", REGION_FIELDS)

HISTORY_FIELDS = ["country", "year", "population"]

top_20 = countries[:20]

history = []
for row in top_20:
    country_html = fetch_page(BASE_URL + row["url"])
    history.extend(scrape_history(country_html, row["country"]))
save_to_csv(history, "history.csv", HISTORY_FIELDS)  