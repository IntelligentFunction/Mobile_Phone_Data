#!/usr/bin/python3
#-*- coding: utf-8 -*-

from datetime import datetime

class Output:


    def _current_rent(self):
        """
        1. Read in the attached file and produce a list 
        sorted by Current Rent in ascending order.
        Obtain the first 5 items from the resultant list 
        and output to the console.
        """
        self.masts.data.sort(key=lambda x: float(x[-1]))
        print(self.masts.header)
        for i in range(5):
            print(self.masts.data[i])
        print()

    def _lease_years(self):
        """
        2. From the list of all mast data create new list 
        of mast data with Lease Years = 25 years.
        Output the list to the console, include all data fields.
        Output the total rent for all items in this list 
        to the console.
        """
        self.lease = []
        self.total_rent = 0
        for i in range(len(self.masts.data)):
            if self.masts.data[i][-2] == 25:
                self.lease.append(self.masts.data[i])
                self.total_rent +=self.masts.data[i][-1]

        print(self.masts.header)
        for i in self.lease:
            print(i)
        print()
        print("Total rent from these masts = {}".
              format(self.total_rent))
        print()

    def _tenant(self):
        """
        3. Create a dictionary containing tenant name and a count 
        of masts for each tenant. 
        Output the dictionary to the console in a readable form.
        
        NOTE. Treat "Everything Everywhere Ltd" and "Hutchinson3G Uk 
        Ltd&Everything Everywhere Ltd" as separate entities.
        """
        self.tenant_dict = {}
        for i in range(len(self.masts.data)):
            cleaned_tenant = self.masts.data[i][6].strip()
            if cleaned_tenant in self.tenant_dict:
                self.tenant_dict[cleaned_tenant] += 1
            else:
                self.tenant_dict[cleaned_tenant] = 1

        for x in self.tenant_dict:
            print(x, self.tenant_dict[x])
        print()

    def _lease_date(self):
        """
        4. List the data for rentals with Lease Start Date 
        between 1 June 1999 and 31 Aug 2007.

        Output the data to the console with dates formatted as 
        DD/MM/YYYY.
        """
        d_start = datetime.strptime("1 Jun 1999","%d %b %Y")
        
        for i in range(len(self.masts.data)):
            start = datetime.strptime(self.masts.data[i][7],
                                      "%d %b %Y")
            if start >= d_start:
                print(self.masts.data[i])
        print()