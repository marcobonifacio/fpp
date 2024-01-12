"""
Data cleansing steps
"""
from collections import Counter
import csv
import doctest
from pathlib import Path

DEFAULT_PATH = Path.cwd() / "address.csv"

def main(source_path: Path = DEFAULT_PATH) -> None:
    """
    Imperative cleasing data steps.

    >>> main()
    Counter({'03801': 1, '12345': 1, '00641': 1, '038011234': 1, '03801-1234': 1, '12345-2345': 1, '00641-1234': 1})
    """
    frequency: Counter[str] = Counter()
    with source_path.open() as source:
        rdr = csv.DictReader(source)
        for row in rdr:
            if "-" in row["ZIP"]:
                text_zip = row["ZIP"]
                missing_zeroes = 10 - len(text_zip)
                if missing_zeroes:
                    text_zip = missing_zeroes * "0" + text_zip
            else:
                text_zip = row["ZIP"]
                if 5 < len(row["ZIP"]) < 9:
                    missing_zeroes = 9 - len(text_zip)
                else:
                    missing_zeroes = 5 - len(text_zip)
                if missing_zeroes:
                    text_zip = missing_zeroes * "0" + text_zip
            frequency[text_zip] += 1
    print(frequency)

def zip_cleanse(text: str) -> str:
    """
    Cleanse zip data.

    >>> zip_cleanse('3801')
    '03801'
    >>> zip_cleanse('12345')
    '12345'
    >>> zip_cleanse('38011234')
    '03801-1234'
    >>> zip_cleanse('3801-1234')
    '03801-1234'
    >>> zip_cleanse('12345-2345')
    '12345-2345'
    """
    if '-' in text:
        return text.zfill(10)
    elif len(text) > 5:
        return f'{text.zfill(9)[:5]}-{text.zfill(9)[5:]}'
    else:
        return text.zfill(5)

def zip_histogram(reader: csv.DictReader[str]) -> Counter[str]:
    """
    Process a csv file returning a Counter object.
    """
    return Counter(zip_cleanse(row['ZIP']) for row in reader)

def main_(source_path: Path = DEFAULT_PATH) -> None:
    """
    Process the file and print the histogram.

    >>> main_()
    Counter({'03801-1234': 2, '03801': 1, '12345': 1, '00641': 1, '12345-2345': 1, '00641-1234': 1})
    """
    with source_path.open() as source:
        rdr = csv.DictReader(source)
        frequency = zip_histogram(rdr)
        print(frequency)

if __name__ == '__main__':
    doctest.testmod()
