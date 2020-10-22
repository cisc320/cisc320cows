import re
from cow import Cow

def main(filepath):
    """
        Reads the inputted txt file line by line and passes a
        parsed record to process_record.

        Args:
            filepath (file): Inputted txt file.
    """
    with open(filepath) as fp:
        for line in fp:
            record = re.split(" ", line)
            if len(record) > 1:
                process_record(record)


def process_record(record):
    """
        Takes in a single parsed record and either creates a new
        cow if the id hasn't been processed before or adds it to
        the existing cow object with the matching id. If it's a new
        cow, adds it to a cow_dict dictionary and a cow_list list.

        Args:
            record (List): Parsed record.
    """
    id = int(record[0])
    if id not in cow_dict:
        new_cow = Cow(id)
        cow_dict[id] = new_cow
        cow_list.append(new_cow)
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
    """
        Prints a the cow if it's get_status doesn't return None.
    """
    for cow in cow_list:
        report = cow.get_status()
        if(report):
            print(report)
            
def partition(arr, low, high):
    """
        Brains of the quicksort. Pivots around the starting index.
        Args:
            array (List): List of non-sorted cows.
            start (int): Start index of focus.
            end (int): Last index of the focus.
        Returns:
            int: New high index.
    """
    i = (low-1)         
    pivot = arr[high]     
 
    for j in range(low, high):
        curr = arr[j]
        if curr.get_lowest_weight() != None and pivot.get_lowest_weight() != None and curr.get_lowest_weight() < pivot.get_lowest_weight():
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
        elif curr.get_lowest_weight() == None or curr.get_lowest_weight() == pivot.get_lowest_weight():
            if curr.get_latest_weight() != None and pivot.get_latest_weight() != None and  curr.get_latest_weight() < pivot.get_latest_weight():
                i = i+1
                arr[i], arr[j] = arr[j], arr[i]
            elif curr.get_latest_weight() == pivot.get_latest_weight():
                if curr.get_avg_milk_prod() < pivot.get_avg_milk_prod():
                    i = i+1
                    arr[i], arr[j] = arr[j], arr[i]
            
    
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

def sort_cows(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        sort_cows(arr, low, pi-1)
        sort_cows(arr, pi+1, high)
        

if __name__ == "__main__":
    cow_dict = {}
    cow_list = []
    main(input())
    sort_cows(cow_list, 0, len(cow_list)-1)
    print_status()