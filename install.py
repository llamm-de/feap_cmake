import time
from progress.bar import IncrementalBar
from os import path, mkdir, chdir, remove
import sys
import glob
from shutil import copyfile
import subprocess


INSTALL_DIR = ""
INSTALL_OPTIONS = {"remove_makefiles": True,
                   "auto_build": True}
DIRECTORIES = ["","contact", "elements" , "main", "packages/arpack", 
               "packages/blas", "packages/lapack", "packages/meshmod", 
               "packages/paraview", "plot", "program", "program/memory", "unix", "user"]

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


def query_install_dir():
    while True:
        answer = str(input("Please enter the directory of your FEAP sources: "))
        if answer == "quit":
            exit()
        elif path.exists(answer) and check_install_dir(answer):
            return answer
        else:
            print("The path you chose does not exist or does not contain any FEAP files!")
            print("Please choose another one or type quit to terminate the process.")


def check_install_dir(dir):
    if path.isfile(dir+"/main/feap84.f") or path.isfile(dir+"/main/feap86.f"):
        return True
    else:
        return False


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
        choice = input(question + prompt).lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")


def setup_install():
    global INSTALL_OPTIONS
    global INSTALL_DIR
    INSTALL_DIR = query_install_dir()
    INSTALL_OPTIONS["remove_makefiles"] = query_yey_or_no("Do you want to remove standard makefiles from FEAP?")
    INSTALL_OPTIONS["auto_build"] = query_yey_or_no("Do you want to automatically build FEAP after setup?", default="yes")


def install():
    global INSTALL_DIR
    global INSTALL_OPTIONS
    global DIRECTORIES
    
    print("Copying CMakeLists.txt files ...")
    bar = IncrementalBar("Progress", max=len(DIRECTORIES))
    for directory in DIRECTORIES:
        src = "files/" + directory + "/CMakeLists.txt"
        dst = INSTALL_DIR + "/" + directory + "/CMakeLists.txt"
        copyfile(src, dst)
        bar.next()
        time.sleep(0.1)
    bar.finish()

    if INSTALL_OPTIONS["remove_makefiles"]:
        print("Removing old makefiles ...")
        bar = IncrementalBar("Progress", max=len(DIRECTORIES))
        for directory in DIRECTORIES:
            file_path = INSTALL_DIR + "/" + directory + "/Makefile"
            try:
                remove(file_path)
            except:
                pass
            bar.next()
            time.sleep(0.1)
        bar.finish()


    if INSTALL_OPTIONS["auto_build"]:

        print("Generating build directory ...")
        if not path.exists(INSTALL_DIR + "/build"):
            mkdir(INSTALL_DIR + "/build")
        else:
            if not query_yey_or_no("Build directory already exists. Do you want to continue anyways?"): 
                exit()
        
        print("Running CMake ...")
        chdir(INSTALL_DIR + "/build")
        subprocess.call(["cmake", ".."])

        print("Building FEAP ...")
        subprocess.call("make")


if __name__ == "__main__": 
    welcome_screen()
    setup_install()
    install()