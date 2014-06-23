"""
SS_Project
Life_Table.py written by: Adam Sarenski
06/2014

Stores the information for Life Expectancy from http://www.ssa.gov/ and returns
"""
import FRA_Table
import csv

def main(sex,age):
    life_table = {}
    if sex == "male":
        sex = 1
    else:
        sex = 2
    with open('Life_Table.csv', 'rb') as f:
        reader = csv.reader(f)
        # skips the header
        reader.next()
        for rows in reader:
            life_table[rows[0]] = [rows[1],rows[2]]
    life = life_table[str(age)]
    return life[sex]