import requests
import csv

#fdownloads page and returns html content
def fetch_page(url):
      headers = {"User-Agent": "Mozilla/5.0"}
      response = requests.get(url, headers=headers)
      if response.status_code == 200:
          return response.text
      return None

def save_to_csv(rows, filename, fields):  #writes data to a CSV file
      with open(filename, "w", encoding="utf-8", newline="") as file:
          writer = csv.DictWriter(file, fieldnames=fields)
          writer.writeheader()
          for row in rows:
              writer.writerow(row)