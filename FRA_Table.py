"""
SS_Project
FRA_Table.py written by: Adam Sarenski
06/2014

Stores the information for FRA from http://www.ssa.gov/ and returns FRA
"""
from datetime import date
from decimal import *

def main(birthdate):
    bd_input = birthdate.year
    years = {
        '1937 or earlier' : 65,
        '1938' : 65 + Decimal(2)/Decimal(12),
        '1939' : 65 + Decimal(4)/Decimal(12),
        '1940' : 65 + Decimal(6)/Decimal(12),
        '1941' : 65 + Decimal(8)/Decimal(12),
        '1942' : 65 + Decimal(10)/Decimal(12),
        '1943-1954' : 66,
        '1955' : 66 + Decimal(2)/Decimal(12),
        '1956' : 66 + Decimal(4)/Decimal(12),
        '1957' : 66 + Decimal(6)/Decimal(12),
        '1958' : 66 + Decimal(8)/Decimal(12),
        '1959' : 66 + Decimal(10)/Decimal(12),
        '1960' : 67,
    }
    if birthdate.year <= 1937:
        return years['1937 or earlier']
    elif birthdate.year >= 1943 and birthdate.year <= 1954:
        return years['1943-1954']
    elif birthdate.year >= 1960:
        return years['1960']
    else:
        return years[str(bd_input)]

# used for testing
# app = main(date(1978, 5, 10))
# print app