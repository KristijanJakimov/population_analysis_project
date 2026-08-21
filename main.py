from helpers import fetch_page, save_to_csv
from countries_scraper import scrape_countries

COUNTRIES_URL = "https://www.worldometers.info/world-population/population-by-country/"
COUNTRY_FIELDS = ["rank", "country", "population", "yearly_change", "net_change","density", "land_area", "migrants", "fertility_rate", "median_age", "urban_pop", "world_share"]

html = fetch_page(COUNTRIES_URL)
countries = scrape_countries(html)
save_to_csv(countries, "countries.csv", COUNTRY_FIELDS)