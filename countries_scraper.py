import re

BLOCK_PATTERN = re.compile(r'<tr id="[^"]*">(.*?)</tr>', re.DOTALL) #turns the pattern into a reusable object
#every Worldometers row is <tr id="india">, <tr id="china">


ROW_PATTERN = re.compile(
    r'<td[^>]*>\s*(?P<rank>\d+)\s*</td>.*?'
    r'<a[^>]*>\s*(?P<country>[^<]+?)\s*</a>.*?'
    r'<td[^>]*>\s*(?P<population>[^<]+?)\s*</td>.*?'
    r'<td[^>]*>\s*(?P<yearly_change>[^<]+?)\s*</td>.*?'
    r'<td[^>]*>\s*(?P<net_change>[^<]+?)\s*</td>.*?'
    r'<td[^>]*>\s*(?P<density>[^<]+?)\s*</td>.*?'
    r'<td[^>]*>\s*(?P<land_area>[^<]+?)\s*</td>.*?'
    r'<td[^>]*>\s*(?P<migrants>[^<]+?)\s*</td>.*?'
    r'<td[^>]*>\s*(?P<fertility_rate>[^<]+?)\s*</td>.*?'
    r'<td[^>]*>\s*(?P<median_age>[^<]+?)\s*</td>.*?'
    r'<td[^>]*>\s*(?P<urban_pop>[^<]+?)\s*</td>.*?'
    r'<td[^>]*>\s*(?P<world_share>[^<]+?)\s*</td>',
    re.DOTALL,    #flag to makes .  match newline characters. without this flag .*? would never reach </tr>. 
)


def parse_row(block_html):
    match = ROW_PATTERN.search(block_html)
    return match.groupdict()

def scrape_countries(html):
    start = html.find("<tbody")
    end = html.find("</tbody>")
    table_body = html[start:end]
    rows = []
    for block in BLOCK_PATTERN.finditer(table_body):
        rows.append(parse_row(block.group(1)))
    return rows