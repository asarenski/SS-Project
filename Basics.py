"""
SS_Project
Basics.py written by: Adam Sarenski
06/2014

Calculates the basic information used for the program.
"""
import datetime
from datetime import date
from decimal import *
import FRA_Table


class Age_Calc():
    """takes date and returns age"""

    def __init__(self, birthdate):
        self.today = date.today()
        self.birthdate = birthdate
        if self.birthdate.month == 2 and self.birthdate.day == 29:
            self.birthdate = date(self.birthdate.year, self.birthdate.month, self.birthdate.day - 1)

    def today_calc(self):
        """Makes sure today is not a leap year."""
        today = self.today
        # if it's 2/29, just return 2/28
        if today.month == 2 and today.day == 29:
            return date(today.year, today.month, today.day - 1)
        else:
            return today

    def age_calc(self):
        """Calculates the age"""
        begin = self.birthdate
        end = self.today_calc()
        age = Decimal((end - begin).days) / Decimal(365.25)
        return age

    def six_two(self, age):
        """Delta to user being sixty-two, takes a float"""
        six_two = round(62 - age)
        return float(six_two)

class Age_List():
    def __init__(self, user_bd, spouse_bd):
        self.user_bd = user_bd
        self.spouse_bd = spouse_bd
        self.today = date.today()

        # create instance of Age_Calc and get user_age and years until 62
        user = Age_Calc(self.user_bd)
        self.user_age = user.age_calc()
        self.user_six_two = user.six_two(self.user_age)

        # create instance of Age_Calc and get spouse_age and years until 62
        spouse = Age_Calc(self.spouse_bd)
        self.spouse_age = spouse.age_calc()

        # find difference in years between user and spouse ages
        self.age_diff = self.user_age - self.spouse_age

        self.date_list = []
        self.user_age_list = []
        self.spouse_age_list = []

    def create_list(self):
        """ Creates date_list, user_age_list, spouse_age_list. Today's date is the datum. """
        for i in range(0, 40):
           self.date_list.append(date(self.today.year+i+int(self.user_six_two), self.today.month, self.today.day))
           self.user_age_list.append(self.user_age+i+int(self.user_six_two))
           self.spouse_age_list.append(self.spouse_age+i+int(self.user_six_two))

def main():
    """sets up and organizes the lists"""

    # sex
    user_sex = "male"
    spouse_sex = "female"

    # dates date need to be in format yyyy, m, d.... ie) no 08
    user_birth_date = date(1998, 06, 17)
    spouse_birth_date = date(2000, 12, 31)

    user_ac = Age_Calc(user_birth_date)
    user_age = user_ac.age_calc()

    spouse_ac = Age_Calc(spouse_birth_date)
    spouse_age = spouse_ac.age_calc()

    # date list
    age_list = Age_List(user_birth_date, spouse_birth_date)
    age_list.create_list()
    date_list = age_list.date_list
    user_age_list = age_list.user_age_list
    spouse_age_list = age_list.spouse_age_list
    age_delt = age_list.age_diff
    age_six = age_list.user_six_two

    print user_age
    print user_birth_date
    print spouse_age
    print spouse_birth_date
    print age_delt
    print age_six
    print date_list
    print user_age_list
    print spouse_age_list

    # retirement numbers
    fra_user = 2600
    seventy_user = 3000
    sixtytwo_user = 1700
    fra_spouse = 2100
    seventy_spouse = 2500
    sixtytwo_spouse = 1200

    # FRA numbers
    fra_age_user = FRA_Table.main(user_birth_date)
    fra_age_spouse = FRA_Table.main(spouse_birth_date)


main()
