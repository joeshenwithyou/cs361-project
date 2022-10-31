# Title: data-microservice.py
# Author: Josiah Potts
# Date Modified: 10-31-2022
# Description: This is a microservice that reads a data.txt file that has an integer, or a float listed
#               line by line and it will calculate the mean and mode of that data and write the results
#               onto a results.txt file for the user to read however they need to.


import time
import os

def calculations():
    """
    function: calculations()
    parameters: None
    returns: None
    pre-conditions: integers or floats written on a data.txt file line by line as strings
    post-conditions: data written on results.txt file
    description: This is the main function used for the microservice of calculating mean and mode of data on the
                text file data.txt. It calls upon mean() and mode() to find calculations and writes the results
                onto the results.txt file.
    """
    #Initialize a list to store data from the data.txt file
    data_list = []

    #Forever loop while software is running
    while True:

        #Clear the list of data for every iteration and wait 5 seconds before running to account for change in data.txt
        data_list.clear()
        time.sleep(5.0)

        #Open data.txt to get the data
        with open("data.txt", "r+") as data_file:
            #Store the data in data_read
            data_read = data_file.readlines()

            #When the data.txt file is empty, skip any calculations. If data is present it will continue
            if os.stat("data.txt").st_size != 0:

                #Open results.txt file and truncate it for an empty file to avoid stale data
                with open("results.txt", "r+") as results_file:
                    results_file.seek(0)
                    results_file.truncate()

                    #Fill the data list with each line of data on data.txt
                    for line in data_read:
                        data_list.append(line)

                    #Store mean calculation into mean_result calling mean() function
                    mean_result = mean(data_list)

                    #Store mode calculation into mode_resut callilng mode() function
                    mode_result = mode(data_list)

                    #Write results of mean calculation on first line of results.txt
                    results_file.writelines("mean=" + str(mean_result) + "\n")

                    #Write results of mode calculation on second line of results.txt, iterate mode_result as there may be multiple modes
                    results_file.writelines("mode=")
                    for i in mode_result:
                        results_file.writelines(str(i) + ",")

        #Close both files.
                results_file.close()
        data_file.close()

def mean(data_list):
    """
    function: mean()
    parameters: A list of strings
    returns: a float
    pre-conditions: None
    post-conditions: None
    description: Takes in a list of strings that represent integers or floats and converts them to floats
                to calculate the mean of the data and returns that mean.
    """
    #Initialize variable to store the sum for calculation
    sum = 0

    #Iterate the values of the data list to calculate the sum
    for i in data_list:
        sum += float(i)

    #Use the sum to divide by the amount of numbers in the list and store the result in mean
    mean = sum / len(data_list)

    #Return the calculated mean
    return mean

def mode(data_list):
    """
    function: mode()
    parameters: A list of strings
    returns: a list of floats
    pre-conditions: None
    post-conditions: None
    description: Takes in a list of strings that represent integers or floats and converts them to floats
                to calculate the mode of the data and returns a list with either 1 mode value or all of the mode values
                if there are ties for mode.
    """
    #Initialize counter at 1 for a single occurance of a number, mode_count, empty list of mode, and data_floats
    counter = 1
    mode_count = 1
    mode = []
    data_floats = []

    #First iterate through the data list to convert them to floats and store them in data_floats list
    for i in data_list:
        data_floats.append(float(i))

    #Sort the list in ascending order to find mode
    data_floats.sort()

    #Iterate length of the list of floats - 1 to account for zero index, and count the mode count
    for x in range(1, len(data_floats)):
        if data_floats[x] == data_floats[x - 1]:
            counter += 1
            if counter > mode_count:
                mode_count = counter
        elif data_floats[x] != data_floats[x - 1]:
            counter = 1

    #Reset the counter variable to 1 for second iteration
    counter = 1

    #Second iteration through length of the list of floats to add all values that match the mode count to the mode list
    for y in range(1, len(data_floats)):
        #Check if all values only occur once
        if mode_count == 1 and y == 1:
            mode.append(data_floats[y - 1])
        if data_floats[y] == data_floats[y - 1]:
            counter += 1
        elif data_floats[y] != data_floats[y - 1]:
            counter = 1
        if counter == mode_count:
            mode.append(data_floats[y])
            counter = 1

    #Special condition handling: if array only has 1 element it automatically is the mode.
    if len(data_floats) == 1:
        mode.append(data_floats[0])

    #Return the list of mode values
    return mode

if __name__ == "__main__":
    calculations()