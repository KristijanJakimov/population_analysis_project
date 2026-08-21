from helpers import fetch_page, save_to_csv
from countries_scraper import scrape_countries
from regions_scraper import scrape_region

COUNTRIES_URL = "https://www.worldometers.info/world-population/population-by-country/"
COUNTRY_FIELDS = ["rank", "country", "population", "yearly_change", "net_change","density", "land_area", "migrants", "fertility_rate", "median_age", "urban_pop", "world_share"]

html = fetch_page(COUNTRIES_URL)
countries = scrape_countries(html)
save_to_csv(countries, "countries.csv", COUNTRY_FIELDS)


REGION_FIELDS = ["country", "continent"]

regions = []
for continent, url in REGION_URLS.items():
    region_html = fetch_page(url)
    regions.extend(scrape_region(region_html, continent))
save_to_csv(regions, "regions.csv", REGION_FIELDS)