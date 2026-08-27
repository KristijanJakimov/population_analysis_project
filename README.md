# Population Analysis Project

This project was created for the course **Introduction to Programming**.

The goal of the project is to collect population data from the web, store it in structured CSV files, and analyze demographic differences between countries and continents using Python, Pandas, and Jupyter Notebook.

## Data Source

The data is collected from **Worldometer**.

The project uses:

- the population-by-country page for current demographic data,
- regional population pages to determine the continent of each country,
- individual country pages for historical population data.

The collected data includes:

- population,
- yearly population change,
- net population change,
- population density,
- land area,
- migration,
- fertility rate,
- median age,
- urban population share,
- world population share,
- continent,
- historical population values.

## Project Structure

- `main.py` – runs the data collection process and creates the CSV files.
- `helpers.py` – contains helper functions for downloading web pages and saving data to CSV.
- `countries_scraper.py` – extracts current demographic data for countries and territories.
- `regions_scraper.py` – extracts the continent of each country.
- `history_scraper.py` – extracts historical population data for the most populated countries.
- `countries.csv` – current demographic data.
- `regions.csv` – country and continent data.
- `history.csv` – historical population data.
- `analysis.ipynb` – contains data cleaning, analysis, graphs, and conclusions.
- `AI_ASSISTANCE.md` – describes how AI was used while reviewing and improving the project.

## Data Collection

The web pages are downloaded using the `requests` library.

The relevant information is extracted from the HTML using regular expressions from Python's `re` module. The extracted data is stored in dictionaries and then saved into CSV files.

To collect the data again, run:

```bash
python main.py
```

## Data Analysis

The analysis is performed in `analysis.ipynb` using Pandas.

The country and region datasets are merged using the country name as the common column, which makes it possible to compare demographic characteristics across continents.

The notebook includes analyses such as:

1. comparison of demographic indicators across continents,
2. fertility rate compared with median age,
3. rankings by population density, urbanization, and population change,
4. distribution of the world population across continents,
5. relationship between land area and population,
6. demographic groups based on fertility, age, and urbanization,
7. migration and natural population growth,
8. historical population growth of the most populated countries.

The results are presented using tables and graphs, followed by short interpretations.

## Required Libraries

The project uses:

- `requests`
- `pandas`
- `matplotlib`

They can be installed with:

```bash
python -m pip install requests pandas matplotlib
```

## Running the Project

1. Clone or download the repository.
2. Install the required libraries.
3. Run `main.py` to download and process the data.
4. Open `analysis.ipynb` in Jupyter Notebook or VS Code.
5. Run the notebook cells from top to bottom.

## Author

Kristijan Jakimov