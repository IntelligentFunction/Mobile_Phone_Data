#!/usb/bin/python3
#-*- coding: utf-8 -*-

import sys
from phone_mast_data import PhoneMastData
from output import Output
class Menu:
    """
    Display a menu and respond to choices when run.
    """

    def __init__(self):
        """
        Initialize Menu
        """
        self.masts = PhoneMastData()
        self.masts._load_data()
        self.output = Output        
        self.choices = {
            "1": self.current_rent,
            "2": self.lease_years,
            "3": self.tenant,
            "4": self.lease_date,
            "5": self.all_functions,
            "6": self.quit
        }

    def display_menu(self):
        print("""
Mobile Phone Mast Data

1. Sort by rent in ascending order and print top 5 items.
2. Print list of mast data with Lease Years = 25 Years.
3. List Tenant name with their current mast count.
4. List rentals with leases dating from 1 June 1999 to 31 Aug 2007.
5. List all the above
6. Quit
""")

        
    def run(self):
        """
        Display the menu then load data and respond to choices.
        """
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))
                

    def current_rent(self):
        """Displays top 5 items in current rent list"""
        self.output._current_rent(self)
        

    def lease_years(self):
        """Displays list of leases of 25 years"""
        self.output._lease_years(self)

        
    def tenant(self):
        """Displays dictionary of tenants and leased masts"""
        self.output._tenant(self)

        
    def lease_date(self):
        """Displays Leases between two dates"""
        self.output._lease_date(self)


    def all_functions(self):
        """Displays all results to console"""
        self.output._current_rent(self)
        self.output._lease_years(self)
        self.output._tenant(self)
        self.output._lease_date(self)

        
    def quit(self):
        print("Mobile Phone Mast application quitting.")
        print("Goodbye")
        sys.exit()

       
    
if __name__ == "__main__":
    app = Menu()
    app.run()
    
