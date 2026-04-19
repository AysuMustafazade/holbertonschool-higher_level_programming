#!/usr/bin/python3
import csv
import json


def convert_csv_to_json(csv_filename):
    """Read a CSV file and write its contents as JSON to data.json.

    Returns True on success, False if the CSV file is not found.
    """
    try:
        with open(csv_filename, 'r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            rows = list(reader)

        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(rows, json_file, indent=4)

        return True

    except FileNotFoundError:
        return False
