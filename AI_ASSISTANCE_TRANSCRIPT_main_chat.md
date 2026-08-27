# AI Assistance Transcript -- World Population Analysis Project

This file documents the questions asked and the guidance received while
developing the Python project. The project collects population data from
Worldometer, stores it in CSV files, and analyzes it in a Jupyter
Notebook.

------------------------------------------------------------------------

## 1. Project idea and workflow

### Question

I'll be working on a Python project which takes information from 1--2
websites, saves the information to a CSV, then analyzes it in a Jupyter
Notebook. Give me a sensible order in which I should work. Everything
must stay at the level of the course material, and the purpose is that I
understand everything, so explain things before giving direct solutions.

### Guidance

The project should be built gradually:

1.  Decide what data is useful.
2.  Inspect the website and its HTML.
3.  Write a simple scraper.
4.  Save the downloaded HTML locally where useful.
5.  Extract the required values.
6.  Save the structured information into CSV files.
7.  Load the CSV files into Pandas.
8.  Clean and inspect the data.
9.  Merge related datasets where necessary.
10. Perform the analysis in Jupyter Notebook.
11. Add graphs and written interpretations.
12. Finish the README and project documentation.

The implementation should remain simple enough to understand and
explain, rather than introducing unnecessarily advanced scraping or
data-analysis techniques.

------------------------------------------------------------------------

## 2. Choosing the population topic

### Question

I was thinking about a population project: how population is distributed
across continents/countries, density, migration, and change with time.
What about Worldometer?

### Guidance

Worldometer is suitable because its population pages contain structured
country-level information useful for this project. A sensible project
can begin with current country statistics and later extend to continent
comparisons and historical population data.

The project can focus on current population distribution first and add
historical analysis later rather than attempting to scrape everything
immediately.

------------------------------------------------------------------------

## 3. Possible analysis topics

### Question

Give me ideas about the topics I'll analyze, maximum 10.

### Guidance

Possible topics include:

-   population by continent;
-   most and least populated countries;
-   population density;
-   urbanization;
-   land area compared with population;
-   fertility rate;
-   median age;
-   migration;
-   yearly population change;
-   historical population development.

The exact questions do not need to be finalized before scraping the
basic dataset.

------------------------------------------------------------------------

## 4. Starting with data before finalizing every question

### Question

Can I start with the code right away, get all the information, and then
decide on the analysis part? I'm not 100% sure about the questions yet.

### Guidance

Yes. It is reasonable to first collect a useful, manageable set of
population variables and then decide which relationships are worth
analyzing.

The important limitation is not to scrape large amounts of information
with no likely use. The main country table already provides enough
variables for many analyses, so it is a good starting dataset.

------------------------------------------------------------------------

## 5. Structure of the scraper

### Question

Keep in mind I'm working in English. Give me an example, but do not code
it, of how a scraper page should look, and remind me of the regex
module.

### Guidance

A simple scraper can conceptually contain:

1.  Imports
2.  Constants such as URLs and file paths
3.  Function for downloading a webpage
4.  Function for saving HTML locally
5.  Function for reading saved HTML
6.  Function for extracting one country row
7.  Function for extracting all country rows
8.  Functions or simple logic for cleaning values
9.  Function for saving the result to CSV
10. A main part that runs the steps

The intended flow is:

`download -> save -> extract -> clean -> save CSV`

Each function should have one clear purpose.

Python's regular-expression module is:

``` python
import re
```

Important regex operations include:

-   `re.search()` -- find the first occurrence;
-   `re.findall()` -- find all occurrences;
-   `re.finditer()` -- iterate over matches;
-   `re.sub()` -- replace matching text;
-   `re.split()` -- split using a pattern.

Useful regex symbols include `\d`, `\s`, `.`, `+`, `*`, `?`, `()`, `[]`,
`^`, and `$`.

For HTML extraction, the difference between greedy `.*` and non-greedy
`.*?` can be important.

------------------------------------------------------------------------

## 6. Inspecting the HTML

### Question

How should I open the HTML so I know how the parts with the countries
look and can write the regex?

### Guidance

Open the saved HTML in a text/code editor such as VS Code. Search for a
known country such as `India`, then locate the surrounding
`<tr> ... </tr>` block.

One table row conceptually looks like:

``` html
<tr>
    <td>...</td>
    <td>India</td>
    <td>...</td>
</tr>
```

The goal is to identify:

-   where one country row starts;
-   where it ends;
-   the order of the `<td>` cells.

Browser Developer Tools can also help understand the structure, but the
saved HTML is particularly important because it represents the content
the scraper actually works with.

------------------------------------------------------------------------

## 7. Choosing the correct Worldometer table

### Question

Which part of the site should I work with? There are multiple tables and
links.

### Guidance

Start with Worldometer's main **Population by Country** table.

It contains the main variables needed for the first dataset, including
country, population, yearly change, density, land area, migrants,
fertility, median age, urban population, and world share.

Ignore live counters, projections, historical tables, and individual
country pages initially. Those can be extensions later.

The first objective is simply:

`main country table -> countries.csv`

------------------------------------------------------------------------

## 8. First countries scraper

### Question

So I should make a countries scraper first, with only the functions
needed?

### Guidance

Yes. Keep the first scraper minimal.

It only needs functionality for:

-   obtaining/saving the HTML;
-   reading it if necessary;
-   extracting country rows;
-   cleaning required values;
-   saving the result to CSV.

Do not add continent analysis, historical scraping, plotting, or
unnecessary abstractions yet.

------------------------------------------------------------------------

## 9. Countries and regions datasets

### Question

I created the main countries data and also a scraper for regions because
I want to work with continents and match countries to regions. Does the
CSV structure look right?

### Guidance

The country dataset structure is appropriate. Useful columns include:

-   rank;
-   country;
-   URL;
-   population;
-   yearly change;
-   net change;
-   density;
-   land area;
-   migrants;
-   fertility rate;
-   median age;
-   urban population;
-   world share.

Keeping each country's URL is useful because it may later be used to
retrieve historical data.

Missing values such as `N.A.` are normal and can be handled during data
preparation.

A separate regions dataset is also reasonable, as long as it provides a
reliable mapping between each country and its continent/region.

------------------------------------------------------------------------

## 10. Beginning the Jupyter Notebook

### Question

Now I would like to start with the notebook. How should I start?

### Guidance

The notebook should begin by understanding the dataset before analyzing
it.

A sensible opening is:

1.  Project title and short description
2.  Import Pandas
3.  Load `countries.csv`
4.  Display a few rows
5.  Check the shape
6.  Check column names
7.  Check data types
8.  Check missing values
9.  Prepare/clean the data
10. Begin analysis

Example opening:

``` python
import pandas as pd

countries = pd.read_csv("data/countries.csv")
countries.head()
```

Markdown cells should explain why each step is being performed.

------------------------------------------------------------------------

## 11. Showing the table

### Question

Should I make a table first?

### Guidance

Yes. Loading the CSV into a Pandas DataFrame is effectively creating the
working table for the notebook.

``` python
countries = pd.read_csv("data/countries.csv")
countries.head()
```

`countries.head()` is useful for verifying that the data loaded
correctly without displaying hundreds of rows.

------------------------------------------------------------------------

## 12. Numeric data stored as text

### Question

I tried calculating the mean and received an error.

### Guidance

Values such as:

`"1,476,625,576"`

may be stored as text because of commas. Percentage values such as
`"0.87%"` are also text.

Before calculations, inspect:

``` python
countries.dtypes
```

Columns used numerically should eventually have numeric types.

------------------------------------------------------------------------

## 13. Inconsistent country names

### Question

Some countries are differently named. How do I correct this?

### Guidance

When two sources use different names for the same country, use a small
manual correction dictionary rather than an unnecessarily complicated
matching system.

Conceptually:

``` python
name_corrections = {
    "USA": "United States",
    "DR Congo": "Democratic Republic of the Congo"
}
```

The purpose is to standardize names before merging datasets.

------------------------------------------------------------------------

## 14. Finding the full list of mismatched country names

### Question

I need to know the full list of countries whose names do not match. How
do I find them?

### Guidance

Convert the country columns to sets and compare them:

``` python
countries_names = set(countries["country"])
regions_names = set(regions["country"])

only_in_countries = countries_names - regions_names
only_in_regions = regions_names - countries_names
```

Display sorted results:

``` python
sorted(only_in_countries)
sorted(only_in_regions)
```

This is much easier than manually comparing hundreds of rows.

After corrections, repeat the comparison. Ideally both differences
become empty.

------------------------------------------------------------------------

## 15. Saint Barthélemy mismatch

### Question

One still shows: Saint Barthelemy.

### Guidance

The likely issue is the accented character:

`Saint Barthélemy`

versus:

`Saint Barthelemy`

Python treats these as different strings.

For a single case, manually standardizing the name is simpler than
implementing a general accent-removal system.

------------------------------------------------------------------------

## 16. Strange symbols in the CSV

### Question

It still isn't fixed. That country has weird symbols in the CSV.

### Guidance

This can indicate an encoding issue, for example a malformed
representation of `é`.

Inspect exactly what Pandas reads:

``` python
countries[countries["country"].str.contains("Bart", na=False)]
```

Use UTF-8 consistently when writing and reading files:

``` python
open(..., encoding="utf-8")
```

and:

``` python
pd.read_csv("countries.csv", encoding="utf-8")
```

If the text was already saved incorrectly, regenerating the CSV with the
correct encoding may be necessary.

------------------------------------------------------------------------

## 17. Quick graph guide

### Question

Give me a quick guide on how to make graphs in the notebook.

### Guidance

Pandas provides simple plotting through:

``` python
data.plot(...)
```

Important graph types:

**Bar chart** -- comparing categories, such as population by continent.

``` python
data.plot(x="continent", y="population", kind="bar")
```

**Line chart** -- change through time.

``` python
history.plot(x="year", y="population", kind="line")
```

**Scatter plot** -- relationships between two numeric variables.

``` python
countries.plot(x="land_area", y="population", kind="scatter")
```

**Pie chart** -- shares of a meaningful total, such as population share
by continent.

A useful workflow is:

`question -> prepare/filter/group data -> table/statistic -> graph -> interpretation`

------------------------------------------------------------------------

## 18. Converting columns to numeric

### Question

How do I make the values strictly numeric?

### Guidance

First remove formatting characters, then convert.

For comma-separated numbers:

``` python
countries["population"] = countries["population"].str.replace(",", "")
countries["population"] = pd.to_numeric(countries["population"])
```

For percentages:

``` python
countries["yearly_change"] = countries["yearly_change"].str.replace("%", "")
countries["yearly_change"] = pd.to_numeric(countries["yearly_change"])
```

When values such as `N.A.` may occur:

``` python
countries["migrants"] = pd.to_numeric(countries["migrants"], errors="coerce")
```

`errors="coerce"` converts invalid numeric values to `NaN`.

------------------------------------------------------------------------

## 19. Excluding zero denominators

### Question

Some countries have rounded values of 0, which causes division by zero.
How can I exclude them?

### Guidance

Filter those rows only for the calculation that requires a nonzero
denominator.

Example:

``` python
valid_countries = countries[countries["land_area"] != 0]
```

Then perform the calculation using `valid_countries`.

The original `countries` DataFrame should remain unchanged.

------------------------------------------------------------------------

## 20. Filtering for a specific table or graph

### Question

What if I need to exclude them only for a specific table or graph?

### Guidance

Create a temporary filtered DataFrame specifically for that analysis:

``` python
density_data = countries[countries["land_area"] != 0]
```

Then use `density_data` for the relevant table or graph.

This avoids permanently removing countries that are useful elsewhere.

------------------------------------------------------------------------

## 21. Final AI transcript documentation

### Question

At the end, will you be able to write a whole Markdown file with our
conversation so I can add it to the project?

### Guidance

Yes. The project can include an AI-assistance/development log containing
the questions, explanations, code snippets, and decisions made during
development.

This document is that record.

------------------------------------------------------------------------

## 22. Merging country and continent information

### Question

How can I merge the information so I can work with continents and
countries?

### Guidance

Use Pandas `merge()` with the country name as the common key.

If `regions` contains the mapping:

`country -> region`

select only those useful columns:

``` python
country_regions = regions[["country", "region"]]
```

Then merge:

``` python
combined = countries.merge(country_regions, on="country")
```

After merging, continent-level analysis can use:

``` python
combined.groupby("region")
```

For example:

``` python
combined.groupby("region")["population"].sum()
```

Always check mismatched country names before merging and compare the
number of rows before and after the merge.

------------------------------------------------------------------------

## 23. Reminder: removing commas

### Question

Shortly remind me how to remove commas from numbers.

### Guidance

``` python
countries["population"] = countries["population"].str.replace(",", "")
countries["population"] = pd.to_numeric(countries["population"], errors="coerce")
```

This changes:

`"1,476,625,576" -> "1476625576" -> 1476625576`

------------------------------------------------------------------------

## 24. Cleaning many numeric columns

### Question

But I have a lot of numbers: migration, land, total population, etc.

### Guidance

Use a simple loop for columns with the same formatting:

``` python
numeric_columns = ["population", "net_change", "land_area", "migrants"]

for column in numeric_columns:
    countries[column] = countries[column].str.replace(",", "")
    countries[column] = pd.to_numeric(countries[column], errors="coerce")
```

Percentage columns can use a separate loop:

``` python
percentage_columns = ["yearly_change", "urban_pop", "world_share"]

for column in percentage_columns:
    countries[column] = countries[column].str.replace("%", "")
    countries[column] = pd.to_numeric(countries[column], errors="coerce")
```

Two simple loops are easier to understand than one complicated cleaning
function.

------------------------------------------------------------------------

## 25. Simple analysis ideas

### Question

Give me ideas about the analysis. Start with simple comparisons.

### Guidance

Useful simple analyses include:

1.  Total population by continent
2.  Number of countries by continent
3.  Average population per country by continent
4.  Average population density by continent
5.  Average urbanization by continent
6.  Total land area by continent
7.  Population versus land area
8.  Top 10 countries by population
9.  Top 10 countries by density
10. Highest and lowest yearly population change

The first few continent comparisons make a good opening.

------------------------------------------------------------------------

## 26. Meaning of median age

### Question

What does median age mean?

### Guidance

Median age is the age that divides a population into two equal halves:

-   50% of people are younger;
-   50% are older.

A lower median age indicates a generally younger population, while a
higher median age indicates an older population.

------------------------------------------------------------------------

## 27. Median age versus average age

### Question

That isn't the same as average age, right?

### Guidance

Correct.

**Average age** is the sum of all ages divided by the number of people.

**Median age** is the middle value after ordering everyone by age.

For:

`10, 20, 30, 40, 100`

the median is `30`, while the average is `40`.

Extreme values affect the average more strongly than the median.

------------------------------------------------------------------------

## 28. Displaying a DataFrame in Jupyter

### Question

If I want the table to show, I just write its name, right?

### Guidance

Yes. If a DataFrame is called:

``` python
continent_population
```

putting:

``` python
continent_population
```

as the last expression in a Jupyter cell displays it as a formatted
table.

------------------------------------------------------------------------

## 29. Important demographic variables to compare

### Question

Which information is most important? For example fertility rate, median
age, migration. Give me two relevant comparisons.

### Guidance

Two strong comparisons are:

-   **fertility rate vs median age**;
-   **migration vs yearly population change**.

A third useful comparison is:

-   **density vs urbanization**.

These are more meaningful than simply ranking every variable
independently.

------------------------------------------------------------------------

## 30. Logical order of comparisons

### Question

Which should come first logically?

### Guidance

A sensible order is:

1.  Fertility rate vs median age
2.  Density vs urbanization
3.  Migration vs yearly population change

In the larger notebook, however, basic population distribution should
come before these demographic relationships.

------------------------------------------------------------------------

## 31. Comparing fertility rate and median age

### Question

How should I compare fertility and median age?

### Guidance

A scatter plot is suitable because both variables are numeric:

``` python
countries.plot(
    x="fertility_rate",
    y="median_age",
    kind="scatter",
    title="Fertility Rate vs Median Age"
)
```

Each dot represents one country.

The analysis looks for a general relationship. A downward pattern would
indicate that higher fertility tends to be associated with lower median
age.

It can also be useful to first calculate continent averages:

``` python
fertility_age = combined.groupby("region")[["fertility_rate", "median_age"]].mean()
```

Then examine individual countries with the scatter plot.

------------------------------------------------------------------------

## 32. README structure

### Question

What should a proper README file contain for later?

### Guidance

A suitable `README.md` can contain:

-   Project title
-   About the project
-   Data source
-   Collected variables
-   Project structure
-   Data collection
-   Data preparation
-   Analysis topics
-   Main findings
-   Technologies used
-   Short instructions for running the project
-   Author

The final README should be written after the project is complete so it
accurately describes what was actually implemented.

------------------------------------------------------------------------

## 33. Is "How to Run" necessary?

### Question

Is a "How to Run" section necessary?

### Guidance

It is not strictly necessary, but a very short section is useful.

For example:

``` markdown
## How to Run

1. Run `scraper.py` to collect the data.
2. Open `analysis.ipynb` in Jupyter Notebook.
```

It does not need to be detailed.

------------------------------------------------------------------------

## 34. Further notebook ideas

### Question

Next ideas about the notebook?

### Guidance

A logical progression is:

-   basic continent overview;
-   fertility and age;
-   density and urbanization;
-   land area;
-   population growth;
-   migration;
-   historical development;
-   conclusions.

Each major section should contain only a few meaningful questions rather
than many repetitive statistics.

------------------------------------------------------------------------

## 35. Population distribution as an introductory analysis

### Question

I was thinking about how population is distributed across the world so
the reader understands the differences between continent populations.

### Guidance

This should come near the beginning.

A section such as **Population Distribution Around the World** can
include:

-   total population by continent;
-   each continent's share of world population;
-   a bar chart for total population;
-   possibly a pie chart for continent shares.

The notebook can then move from:

`where people live -> how densely they live -> demographic structure -> population change`

------------------------------------------------------------------------

## 36. Going beyond obvious rankings

### Question

I added population distribution and rankings showing which countries top
each metric. I was thinking about countries such as Russia, which are
big on a map but mostly unpopulated, or the opposite. I also need a
topic that isn't obvious directly from the website.

### Guidance

A useful next section is **Land Area vs Population**.

Use a scatter plot with:

-   x-axis: land area;
-   y-axis: population.

Then inspect outliers: countries with enormous territory but relatively
small populations, and countries with relatively small territory but
very large populations.

Other derived-analysis ideas included:

-   population concentration within continents;
-   migration relative to population;
-   migration compared with population growth;
-   demographic profiles based on multiple variables.

The aim is to derive information rather than simply reproduce rankings
already visible on Worldometer.

------------------------------------------------------------------------

## 37. Population concentration within continents

### Question

Explain more about the first suggestion.

### Guidance

The idea was to ask whether a continent's population is distributed
across many countries or concentrated in a few.

For example:

`population of top 3 countries / total continent population * 100`

This would measure how much of a continent's population lives in its
largest countries.

However, this metric has an important limitation: continents have very
different numbers of countries.

------------------------------------------------------------------------

## 38. Is concentration comparison fair?

### Question

Does that comparison really seem logical? Europe has many countries,
South America far fewer, and Oceania even fewer.

### Guidance

This criticism is correct.

Using a fixed "top 3" is not fully fair across continents because the
number and size of countries differ greatly.

A more comparable approach could use the top percentage of countries,
but that becomes more complicated.

For this project, a simpler and stronger alternative is land area versus
population, because it is easier to explain and does not require
designing an arbitrary concentration measure.

------------------------------------------------------------------------

## 39. Simpler middle sections before history

### Question

That seems complicated. Explain your other ideas. One section will be a
brief history analysis near the end, but I still need 2--3 sections in
between.

### Guidance

Three suitable middle sections are:

### Land area vs population

Ask whether physically larger countries necessarily have larger
populations and identify outliers.

### Fertility rate vs median age

Study population structure and the relationship between fertility and
how young or old a population is.

### Migration vs population change

Study whether countries with positive or negative migration are growing
or declining.

Then finish with historical population analysis.

A coherent notebook structure becomes:

1.  Population distribution
2.  Rankings
3.  Land area vs population
4.  Fertility rate vs median age
5.  Migration vs population change
6.  Historical population change
7.  Conclusion

------------------------------------------------------------------------

## 40. Migration vs population change

### Question

Explain the third idea.

### Guidance

The main question is:

**How does migration relate to whether a country's population grows or
shrinks?**

Useful variables are:

-   `migrants`;
-   `yearly_change` or `net_change`.

Possible combinations include:

-   positive migration + positive growth;
-   negative migration + positive growth;
-   positive migration + population decline;
-   negative migration + population decline.

A scatter plot can compare:

``` python
countries.plot(
    x="migrants",
    y="yearly_change",
    kind="scatter"
)
```

Raw migration values should be interpreted carefully because the same
number of migrants has a different impact on small and large countries.

------------------------------------------------------------------------

## 41. Other migration-analysis ideas

### Question

Other suggestions about this topic?

### Guidance

Possible migration analyses include:

-   which continents gain or lose the most people through migration;
-   countries growing despite negative migration;
-   countries declining despite positive migration;
-   fertility and migration together;
-   migrants per 1,000 inhabitants.

The particularly interesting cases are exceptions such as:

`negative migration + population growth`

and:

`positive migration + population decline`

because they show that population change cannot be explained by
migration alone.

------------------------------------------------------------------------

## 42. Classifying countries into categories

### Question

You also mentioned analyzing countries based on which category they
belong in.

### Guidance

Countries can be classified using combinations of variables.

For fertility and median age, an example analytical classification is:

-   young + high fertility;
-   young + low fertility;
-   older + high fertility;
-   older + low fertility.

For migration and growth:

-   positive migration + growing;
-   negative migration + growing;
-   positive migration + declining;
-   negative migration + declining.

These are analytical categories created for the project, not necessarily
official demographic classifications.

------------------------------------------------------------------------

## 43. Searching for related demographic concepts

### Question

How should I correctly search the internet to find related information
as inspiration?

### Guidance

For general population-analysis inspiration, useful sources and concepts
include population distribution, demographic indicators, migration,
fertility, and population growth.

However, when searching for the specific idea of classifying countries
into groups, more precise demographic terminology is preferable.

------------------------------------------------------------------------

## 44. Correct name for the classification idea

### Question

No, I meant the exact topic about categories. How are they correctly
named?

### Guidance

Useful terms include:

-   **demographic profiles**;
-   **demographic typology**;
-   **population age structure and fertility**;
-   **demographic transition**;
-   **Demographic Transition Model (DTM)**;
-   **components of population change**;
-   **natural increase and net migration**;
-   **population growth and net migration typology**.

The four groups suggested for the notebook are a simple project-specific
classification rather than an official demographic standard.

------------------------------------------------------------------------

## 45. Showing example countries at the start

### Question

Could I first show 4--5 countries as examples in the first cell of the
notebook?

### Guidance

Yes. This can help the reader understand what one row contains before
seeing the full analysis.

Choose countries with noticeably different characteristics, for example:

-   India -- very large population;
-   Russia -- very large land area;
-   Bangladesh -- high density;
-   Germany -- older population/lower fertility;
-   Nigeria -- younger population/higher fertility.

Example selection:

``` python
example_countries = countries[
    countries["country"].isin(
        ["India", "Russia", "Bangladesh", "Germany", "Nigeria"]
    )
]

example_countries
```

This can be more informative than simply displaying `countries.head()`.

------------------------------------------------------------------------

## 46. Functions for differentiating countries

### Question

How could I write functions that differentiate them and then apply them?

### Guidance

For a category based on conditions, write a function that receives one
DataFrame row, checks the relevant variables, and returns a category.

Pandas can then apply that function row by row using:

``` python
countries.apply(function_name, axis=1)
```

`axis=1` means that the function is applied to each row.

------------------------------------------------------------------------

## 47. Fertility and median-age categories

### Question

No, I meant the categories.

### Guidance

For fertility and median age, one simple method is to use the dataset
medians as cutoffs rather than inventing arbitrary thresholds.

First calculate:

``` python
fertility_median = countries["fertility_rate"].median()
age_median = countries["median_age"].median()
```

Then define:

``` python
def demographic_category(row):
    if row["fertility_rate"] >= fertility_median and row["median_age"] < age_median:
        return "Young, high fertility"

    elif row["fertility_rate"] < fertility_median and row["median_age"] < age_median:
        return "Young, low fertility"

    elif row["fertility_rate"] >= fertility_median and row["median_age"] >= age_median:
        return "Older, high fertility"

    else:
        return "Older, low fertility"
```

Apply it:

``` python
countries["demographic_category"] = countries.apply(
    demographic_category,
    axis=1
)
```

Then inspect:

``` python
countries[
    ["country", "fertility_rate", "median_age", "demographic_category"]
]
```

or count categories:

``` python
countries["demographic_category"].value_counts()
```

The notebook should clearly state that these are project-defined
analytical categories based on whether values are above or below the
dataset median, not an official demographic classification.

------------------------------------------------------------------------

# Overall project direction

The project evolved toward the following structure:

1.  **Collect current country population data**
2.  **Collect country-to-continent/region information**
3.  **Store both datasets in CSV files**
4.  **Clean and standardize the data in Pandas**
5.  **Merge country and continent information**
6.  **Introduce the dataset with representative countries**
7.  **Analyze world population distribution**
8.  **Show basic country rankings**
9.  **Compare land area and population**
10. **Analyze fertility rate and median age**
11. **Analyze migration and population change**
12. **Perform a brief historical population analysis**
13. **Summarize conclusions**
14. **Complete README and project documentation**

The guiding principle throughout development is to keep the Python
implementation within the level of the course material and to understand
the purpose of each function, Pandas operation, calculation, and graph
rather than using unnecessarily advanced solutions.
