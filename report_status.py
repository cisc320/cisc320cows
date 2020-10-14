import sys
import os
import re
from cow import Cow

def main(filepath):
    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting...".format(filepath))
        sys.exit()
    with open(filepath) as fp:
        for line in fp:
            record = re.split(" ", line)
            process_record(record)

def process_record(record):
    id = int(record[0])
    if id not in cow_dict:
        cow_dict[id] = Cow(id)
    cow = cow_dict[id]
    action = record[1]
    value = int(record[2])
    if action == "M":
        cow.add_milk(value)
    elif action == "W":
        cow.set_weight(value)
    elif action == "T":
        cow.set_temperature(value)

def print_status():
    for cow in cow_dict.values():
        report = cow.get_status()
        if(report):
            print(report)

if __name__ == '__main__':
    cow_dict = {}
    main("/Users/philipoconnor/Desktop/phil.txt")
    print_status()