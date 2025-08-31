"""
 Name         : county_info.py
 Author       : Matthew Stevens
 Created      : Creation Date 7-5-2025
 Course       : CIS189
 IDE          : Visual Studio Code
 Description  : The purpose of this program is to read Iowa census data from CSV,
               input is County objects, and output the population of all counties.

 Academic Honesty: I attest that this is my original work.
 I have not used unauthorized source code, either modified or
 unmodified.
"""

import csv

class County:
    def __init__(self, rank, name, per_capita_income, median_household_income,
                 median_family_income, population, number_of_households):
       
        self.rank = rank
        self.name = name
        self.per_capita_income = self.clean_currency(per_capita_income)
        self.median_household_income = self.clean_currency(median_household_income)
        self.median_family_income = self.clean_currency(median_family_income)
        self.population = self.clean_number(population)
        self.number_of_households = self.clean_number(number_of_households)

    def get_population(self):
        """
        Return population 
        """
        return self.population

    def __repr__(self):
        return (f"County({self.rank}, '{self.name}', {self.per_capita_income}, "
                f"{self.median_household_income}, {self.median_family_income}, "
                f"{self.population}, {self.number_of_households})")

   
    def clean_currency(value):
        """
        Remove dollar signs and commas
        """
        return float(value.replace('$', '').replace(',', '').strip())

   
    def clean_number(value):
        """
        Remove commas 
        """
        return int(value.replace(',', '').strip())

def main():
    total_population = 0
    counties = {}

    with open(r"C:\mathewstevens.info\cis189python\module_12\Iowa 2010 Census Data Population Income.csv", newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            county_name = row['County'].strip()
            if county_name in ['United States', 'Iowa State'] or county_name == '':
                continue  # Skip aggregate rows or empty rows

            # County object
            county = County(
                rank=row['Rank'],
                name=county_name,
                per_capita_income=row['Per capita income'],
                median_household_income=row['Median household income'],
                median_family_income=row['Median Family Income'],
                population=row['Population'],
                number_of_households=row['Number of households']
            )

            counties[county_name] = county
            total_population += county.get_population()

    print(f"Total population of all Iowa counties: {total_population:,}")

if __name__ == "__main__":
    main()
