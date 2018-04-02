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
            if self.masts.data[i][6] in self.tenant_dict:
                self.tenant_dict[self.masts.data[i][6]] += 1
            else:
                self.tenant_dict[self.masts.data[i][6]] = 1

        for x in self.tenant_dict:
            print(x," "*(50-len(x)), self.tenant_dict[x])
        print()

        
    def _lease_date(self):
        """
        4. List the data for rentals with Lease Start Date 
        between 1 June 1999 and 31 Aug 2007.

        Output the data to the console with dates formatted as 
        DD/MM/YYYY.
        """
        d_start = datetime.strptime("1 Jun 1999","%d %b %Y")
        print(
            "Property Name"," "*27,
            "Client Name"," "*39,
            "Start Date"," "*10,
            "End Date"," "*12
        )

        for i in range(len(self.masts.data)):
            start = datetime.strptime(self.masts.data[i][7],
                                      "%d %b %Y")
            #s_format = datetime.strptime(
            #    self.masts.data[i][7], "%d %b %Y").strftime("%d/%m/%Y")
            if start >= d_start:
                x = self.masts.data[i]
                print(
                    x[0]," "*(40-len(x[0])),
                    x[6]," "*(50-len(x[6])),
                    datetime.strptime(x[7], "%d %b %Y").
                    strftime("%d/%m/%Y"),
                    " "*(11-len([7])),
                    datetime.strptime(x[8], "%d %b %Y").
                    strftime("%d/%m/%Y")
                )
        print()
