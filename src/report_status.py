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


def partition(array, start, end):
    """
        Brains of the quicksort. Pivots around the starting index.

        Args:
            array (List): List of non-sorted cows.
            start (int): Start index of focus.
            end (int): Last index of the focus.
        Returns:
            int: New high index.
    """
    pivot = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high:
            curr = array[high]
            if curr.get_lowest_weight() > pivot.get_lowest_weight():
                high -= 1
            elif curr.get_lowest_weight() == pivot.get_lowest_weight():
                if curr.get_latest_weight() > pivot.get_latest_weight():
                    high -= 1
                elif curr.get_latest_weight() == pivot.get_latest_weight():
                    if curr.get_avg_milk_prod() > pivot.get_avg_milk_prod:
                        high -= 1
                    else:
                        break
                else:
                    break
            else:
                break

        while low <= high:
            curr = array[low]
            if curr.get_lowest_weight() < pivot.get_lowest_weight():
                low += 1
            elif curr.get_lowest_weight() == pivot.get_lowest_weight():
                if curr.get_latest_weight() < pivot.get_latest_weight():
                    low += 1
                elif curr.get_latest_weight() == pivot.get_latest_weight():
                    if curr.get_avg_milk_prod() < pivot.get_avg_milk_prod:
                        low += 1
                    else:
                        break
                else:
                    break
            else:
                break

        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high


def sort_cows(array, start, end):
    """
        Recursive quicksort function.

        Args:
            array (List): List of non-sorted cows.
            start (int): Start index of list.
            end (int): Last index of the list.
    """
    if start >= end:
        return
    p = partition(array, start, end)
    sort_cows(array, start, p-1)
    sort_cows(array, p+1, end)

if __name__ == "__main__":
    cow_dict = {}
    cow_list = []
    main(input())
    sort_cows(cow_list, 0, len(cow_list)-1)
    print_status()