# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import re
from Beacon import *

is_scanning = False
is_opened = False
scan_start_time = 0;
Beacons = []


def main():
    file = open("IPS_test.txt", "r")
    if file.readable():
        print("============")
        print("Beginning of file")
    while True:
        line = file.readline()
        if not line:
            print("End of File")
            print("=============")
            break
        analyse(file.readline())


def analyse(line):
    global is_opened
    global is_scanning
    global scan_start_time
    if line == "\n":
        if is_scanning:
            print("Scanning was never Stopped.")
        if is_opened:
            print("File was never closed.")
        is_scanning = False
        is_opened = False

    prompts = re.split(" ", line)
    origin = prompts[0]
    time = float(prompts[2])
    command = prompts[3]

    if origin == "native-lib":
        if command == "File_Opened":
            if is_opened:
                print("New reference to file opened. File was never closed.")
            is_opened = True
        elif command == "Scanning_Started":
            if is_scanning:
                print("New Scan started. But previous scan was never stopped.")
            scan_start_time = time
            is_scanning = True
        elif command == "Stopping_Scan":
            is_scanning = False
        elif command == "Scanning_Stopped":
            is_scanning = False
            scan_start_time = 0
        elif command == "File_Closed":
            is_opened = False
            scan_start_time = 0

    elif origin == "Beacon.h":
        if command == "Beacon_Added":
            major = int(prompts[4])
            minor = int(prompts[5])
            for beacon in Beacons:
                if (beacon.__getattribute__(major) == major) & (beacon.__getattribute__(minor) == minor):
                    print("Beacon was already added.")
                    return
            time_diff = time - scan_start_time
            Beacons.append(Beacon.from_maj_min_time(major, minor, time_diff))
        elif command == "Updating_Beacon":
            print()

    elif origin == "Rssi.h":
        print()

    else:
        print("Origin not defined")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
