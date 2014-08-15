# Linear regression library
import linearreg as lr

# .csv file manipulation
import csv

# Time conversion libraries
import time
import datetime

# Used for list copy
from copy import deepcopy

def analysetrend(filename = "table.csv", output_filename = "trend.csv", regression_threshold = 0.8) :
    #-------------------------------------------------------------------------------------------------------
    # Variable declarations


    # Output of .csv file reading
    date_list = []
    price_list = []

    # Copies of previous lists, used for data manipulation
    date_list_copy = []
    price_list_copy = []

    # Series of regressions approximating price_list
    # Format : [[slope, origin point, R squared], number of points]
    regressions = []

    # List of prices calculated from the regression list
    trend_price_list = []

    # Used for X axis offsetting
    day_offset = 0

    #-------------------------------------------------------------------------------------------------------


    #Open and read a .csv file
    csv_file = open(filename)
    csv_input = csv.reader(csv_file)


    # Parse then close the file
    for row in csv_input :
        try :
            # Read and convert the date and price
            if day_offset == 0 :
                day_offset = time.mktime(datetime.datetime.strptime(row[0], "%Y-%m-%d").timetuple())/86400
            date_list.append(time.mktime(datetime.datetime.strptime(row[0], "%Y-%m-%d").timetuple())/86400 - day_offset + 1)
            price_list.append(float(row[-1]))
            # If a line is not a data line (e.g. a column name line), it is skipped
        except ValueError :
            print("Skipping line")
    csv_file.close()


    # Copy the date and price lists for manipulation
    date_list_copy = deepcopy(date_list)
    price_list_copy = deepcopy(price_list)

    # Find the set of regressions associated with the parsed data
    while len(date_list_copy) > 1 :
        # Use a linear regression on the leftmost part of the data, store the result
        regression_results = lr.partialreg(date_list_copy, price_list_copy, regression_threshold)
        regressions.append(regression_results)
        # Delete data used in previous regression
        del date_list_copy[:regression_results[1]]
        del price_list_copy[:regression_results[1]]



    # Interpolate the trend prices
    for reg in regressions :
        for i in range(0,reg[1]) :
            l = len(trend_price_list)
            trend_price_list.append(reg[0][0] * date_list[l] + reg[0][1])
		
    # Adjust for potential loss of rightmost point during the regression phase
    if len(trend_price_list) < len(date_list) :
        trend_price_list.append(price_list[-1])

    # Write results to .csv file
    with open("trend.csv", "w+", newline='') as f:
        writer = csv.writer(f)
        writer.writerows(zip(date_list, price_list, trend_price_list))

    return regressions, trend_price_list