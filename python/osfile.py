#
# Example file for working with os.path module
# LinkedIn Learning Python course by Joe Marini
#

import os
from os import path
import datetime
from datetime import date, time, timedelta
import time


def main():
    # Print the name of the OS
    print(os.name)
    
    # Check for item existence and type
    print("item exits:", str(path.exists("j.txt")))
    print("iem is a file:",path.isfile("j.txt"))
    print("iem is a directory:",path.isdir("j.txt"))

    # Work with file paths
    print("item's path", path.realpath("j.txt"))
    print("item's path and name:",path.split(path.realpath("j.txt")))
    
    # Get the modification time
    t=time.ctime(path.getmtime("j.txt"))
    print(t)
    print(datetime.datetime.fromtimestamp(path.getmtime("j.txt")))
    
    # Calculate how long ago the item was modified
    td= datetime.datetime.now()-datetime.datetime.fromtimestamp(path.getmtime("j.txt"))
    print("it has been",td,"since the file was mofified")
    print("Or,",td.total_seconds(),"seconds")
if __name__ == "__main__":
    main()
