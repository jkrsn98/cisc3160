## l2: some exercises

### 1: shell script to sort csv file
Given a csv file formatted as Name, Age, Major, GPA, the script extracts the name and GPA and sorts the values by GPA.

To run, enter ``./sort.sh`` with mycsv.csv in the directory

**Example of expected behaviour:**
Given the following .csv file,
```
John, 25, History, 3.8
Jane, 30, Biology, 3.6
```
Running the script will return
```
CONTENTS OF CSV FILE:
John, 25, History, 3.8
Jane, 30, Biology, 3.6

NAME AND GPA SORTED BY GPA:
Jane, 3.6
John, 3.8
```

### 2: python temperature conversions
Given an array of temperatures and their respective units, the program converts each temperature to the opposite unit.

To run, enter ``py tempConversion.py`` 

**Example of expected behaviour:**
Given the following definition of tempArr,
```
tempArr = [ Temperature(44, "f"), Temperature(2, "c"), Temperature(12, "f") ]
```
Running the program will return
```
TEMPERATURE ARRAY
44 f
2 c
12 f

TEMPERATURES CONVERTED:
6.7 c
35.6 f
-11.1 c

```


### 3. js API request
Script accesses the [Bored API](https://www.boredapi.com/) to return an activity that you may want to do if you're bored.

To run, enter ``npm i axios``, then ``node apiRequest.js``

**Example of expected behaviour:**
```
Create a cookbook with your favorite recipes
```
