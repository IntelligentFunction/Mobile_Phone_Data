#!/usb/bin/python3
#-*- coding: utf-8 -*-

import sys
from phone_mast_data import PhoneMastData


class Menu:
    """
    Display a menu and respond to choices when run.
    """
    def __init__(self):
        self.data = PhoneMastData
        self.choices = {
            "1": self.current_rent,
            "2": self.lease_years,
            "3": self.tenant,
            "4": self.lease_date,
            "5": self.quit
        }

    def display_menu(self):
        print("""
Mobile Phone Mast Data

1. Sort by rent in ascending order and print top 5 items.
2. Print list of mast data with Lease Years = 25 Years.
3. List Tenant name with their current mast count.
4. List rentals with leases dating from 1 June 1999 to 31 Aug 2007.
5. Quit
""")

    def run(self):
        """Displat the menu and respond to choices."""
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def current_rent(self):
        self.masts = PhoneMastData()
        self.masts.load_data()
        print(self.masts.header)
        for i in range(5):
            print(self.masts.data[i])


    def lease_years(self):
        pass


    def tenant(self):
        pass


    def lease_date(self):
        pass


    def quit(self):
        print("Mobile Phone Mast application quitting.")
        print("Goodbye")
        sys.exit()


if __name__ == "__main__":
    Menu().run()
