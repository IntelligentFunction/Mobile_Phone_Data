#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys
from csv import reader

class PhoneMastData:
    """
    Initialize data list with an empty list
    """
    
    def __init__(self):
        #self.header = []
        self.data = []

        
    def _load_data(self):
        '''
        Function to load data into program
        '''
        self.path = sys.argv[1]
        try:
            with open(self.path, newline='') as self.myfile:
                self.reader = reader(self.myfile)
                self.header = (next(self.reader))
                for row in self.reader:
                    property = str(row[0])
                    address1 = str(row[1])
                    address2 = str(row[2])
                    address3 = str(row[3])
                    address4 = str(row[4])
                    unit = str(row[5])
                    tenant = str(row[6])
                    start = str(row[7])
                    end = str(row[8])
                    years = int(row[9])
                    rent = float(row[10])
                    
                    self.data.append([property, address1, address2,
                                      address3, address4, unit, tenant,
                                      start, end, years, rent])
        except:
            print()
            print("Error reading data file, please check data file and try again.")
            print()
            print("Quitting application")
            print()
            sys.exit()

if __name__ == "__main__":
    app = PhoneMastData()
    app.run()
