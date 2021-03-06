# cows

**Problem:** Calculate, sort, and report minimum, most recent, and average of a sequence of records.

**Input:** The filename of a local file containing a sequence of cow records, each on their own line. The first line will be the number of records to read, and is not included in the number of records. You can assume that each line will only contain one record. The records will come in ordered by the time they were collected.

A cow record consists of three numbers and a letter, separated by spaces (in the form "Number, Letter, Number, Number"). All numbers will be 32-bit integers (i.e., no more than 2^31).

- The first element is the Cow ID, a unique number representing that cow inside the dataset.
- The second element is the Action Code, and will be either the letter "W", "M", or "T"
- If the letter is "W", for "Weighing", then the third element will be the latest Weight of the cow (a number in pounds).
- If the letter is "M", for "Milking", then the third element will be the amount of the Milk produced by the cow (a number in pounds).
- If the letter is "T", for "Temperature", then the third element will be the current Temperature of the cow (a number in Fahrenheit).
- The fourth element is the Timestamp, a number representing when the record was made.

An example of several records are below:

```
507 W 1000 1
1 M 6 2
1 W 1400 3
1 M 8 8
1 T 101 10
507 M 4 12
1 W 1700 15
1 M 7 16
507 M 8 20
```

**Output:** A series of sorted cow status reports. Each line of output will contain four numbers:

The cow's ID
The cow's lowest weight
The cow's latest weight
The cow's average milk production (the sum of all the milkings divided by the number of milkings).
If a cow doesn't have at least one weighing and at least one milking, then you should exclude it from the output. The cows should be sorted in ascending order based the status results: first by their lowest weight, than their latest weight, and finally by their average milk production. Truncate any decimals to become integers.

An example of output is below:

```
507 1000 1000 6
1 1400 1700 7
```

------

Solution

To input a cow we use a dictionary to find the cow given its ID. If it is not in the dictionary then it makes a new key:value pair and appends the cow to a list of cows, if it is in the dictionary we can update the relevant information. Since a dictionary is O(1) each time we input a record it will be O(1). Therefore the time complexity for inputing r number of rows is r.

To sort the cows we used the quicksort algorithm which has an average case of O(n log(n)). Therefore the average case given c number of cows is O(c log(c)).

Therefore since we used the quicksort algorithm in addition to using a dictionary to input rows, we have an average case of O(c log(c) + r).

When printing the sorted list of cows we check if the cow has at least one weight and one milking. This takes  O(c), but since this is a constant we can ignore this. Therefore the average case is still O(c log(c) + r).
