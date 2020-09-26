import time
from progress.bar import IncrementalBar
from os import path
import sys


INSTALL_DIR = ""
INSTALL_OPTIONS = {"remove_makefiles": False,
                   "auto_build": False}

def welcome_screen():
    print("\n ______ ______          _____  __  __          _  ________")
    print(r"|  ____|  ____|   /\   |  __ \|  \/  |   /\   | |/ /  ____|")
    print(r"| |__  | |__     /  \  | |__) | \  / |  /  \  | ' /| |__   ")
    print(r"|  __| |  __|   / /\ \ |  ___/| |\/| | / /\ \ |  < |  __|  ")
    print(r"| |    | |____ / ____ \| |    | |  | |/ ____ \| . \| |____ ")
    print(r"|_|    |______/_/    \_\_|    |_|  |_/_/    \_\_|\_\______|")
    print("\nWelcome to the installation of CMake support for FEAP!\n")                                                        


def display_progress_bar(items, label="Progress"):
    bar = IncrementalBar(label, max=len(items))
    for _ in items:
        bar.next()
        time.sleep(0.1)
    bar.finish

def set_install_dir():
    INSTALL_DIR = str(input("Please enter the directory of your FEAP sources: "))
    if not path.exists(INSTALL_DIR):
        print("The path you chose does not exist!")
        print("The process is terminated!")
        exit()

def set_install_options():
    INSTALL_OPTIONS["remove_makefiles"] = query_yey_or_no("Do you want to remove standard makefiles from FEAP?")
    INSTALL_OPTIONS["auto_build"] = query_yey_or_no("Do you want to automatically build FEAP after setup?")

def query_yey_or_no(question, default="no"):
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")

if __name__ == "__main__": 
    #welcome_screen()
    #set_install_dir()
    set_install_options()
    #mylist = [1,2,3,4,5,6,7,8]
    #display_progress_bar(mylist, label="Copying CMake files ")