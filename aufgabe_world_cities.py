# Lese die Datei worldcities.csv mit dem CSV - Reader ein,
# sortiere die Einträge nach city_ascii und speichere sie in einer
# neuen Daten worldcities_sorted.csv ab.
# Schreibe dazu die Funktion load_cities, sort_cities_by_ascii_name und
# save_cities_to_file.

# 1.b) Länder-Filter
# Erweitere die Aufgabe um einen Länder-Filter: es sollen nur Einträge
# in die neue Datei kommen, die einem eingegebenen Land entsprechen (zb. India)

import csv
from pathlib import Path


def load_cities(filename):
    with open(Path(__file__).parent / filename, encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=",")
        result = list(reader)
    return result


def sort_cities_by_ascii_name(reader_sort, filter_country=None):
    if filter_country:
        result = list(filter(lambda e: e["country"] in filter_country, reader_sort))
        result = sorted(result, key=lambda e: e["city_ascii"])
    else:
        result = sorted(reader_sort, key=lambda e: e["city_ascii"])
    return result


def save_cities_to_file(filename_name, liste_sorted):
    with open(Path(__file__).parent / filename_name, mode="w", newline="", encoding="utf-8") as f:
        fieldnames = ["city", "city_ascii", "lat", "lng", "country", "iso2",
                      "iso3", "admin_name", "capital", "population", "id"]
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=",")
        writer.writeheader()
        writer.writerows(liste_sorted)


def main():
    countryinput = input("Nach welchem Land filtern(Eingabe = Y, Land)?: ").split(",")
    if countryinput.pop(0) == "Y":
        save_cities_to_file(f"worldcities_sorted_{'-'.join(countryinput)}.csv", sort_cities_by_ascii_name(load_cities("worldcities.csv"), countryinput))
    else:
        save_cities_to_file("worldcities_sorted_.csv", sort_cities_by_ascii_name(load_cities("worldcities.csv")))
    

main()
