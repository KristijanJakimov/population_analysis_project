import re

COUNTRY_PATTERN = re.compile(r'<li>\s*<a[^>]*>\s*(?P<country>[^<]+?)\s*</a>\s*</li>', re.DOTALL)

def scrape_region(html, continent):
    rows = []
    for match in COUNTRY_PATTERN.finditer(html):
        rows.append({"country": match.group("country"), "continent": continent})
    return rows