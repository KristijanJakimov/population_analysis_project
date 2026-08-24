import re

ROW_PATTERN = re.compile(
    r'<tr>\s*<td[^>]*>\s*(?P<year>\d+)\s*</td>'
    r'<td[^>]*>\s*(?P<population>[\d,]+)\s*</td>',
    re.DOTALL,
)


def scrape_history(html, country):
    start = html.find("and historical)</h2>")
    end = html.find("Population Forecast</h2>")
    table_html = html[start:end]
    rows = []
    for match in ROW_PATTERN.finditer(table_html):
        rows.append({
            "country": country,
            "year": match.group("year"),
            "population": match.group("population"),
        })
    return rows
