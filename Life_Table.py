"""
SS_Project
Life_Table.py written by: Adam Sarenski
06/2014

Stores the information for Life Expectancy from http://www.ssa.gov/ and returns
"""
import FRA_Table
import csv

def main(sex,age):
    with open('Life_Table.ods', 'rb') as LT:
        LTreader = csv.reader(LT, delimiter=' ', quotechar='|')
        for row in LTreader:
            print ', '.join(row)
main('male', 65)