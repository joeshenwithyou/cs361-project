# Mean And Mode Calculator Microservice

Description of program:

This program operates individually and while running it will periodically read a text file in the directory, 
titled "data.txt" and it will read it for usable data such as numbers or decimal values. The program will then 
use that data to calculate the mean and mode(s) of the data. Then, it will write the results on the first two 
lines of another text file called "results.txt" for the user of the microservice to read and use how they desire.

How to REQUEST data from this microservice:

1. Make sure data-microservice.py, data.txt, results.txt and your program are in the same directory.
2. Run data-microservice.py.
3. Include a segment of code in your program that truncates the data.txt file, and writes new data onto the
data.txt file.
  Data written onto data.txt must be in this format:
    - Each line of data.txt should contain a single number or decimal value (recommended loop iteration through an array)
    - Exclude any non-numerical characters (i.e. letters, symbols besides one ".")
    - Does not need to be sorted
4. Run your program.

 -----EXAMPLE CALL-----
   
    data_list = ["15", "25", "80", "80", "20", "1", "1", "1", "24.5"]

    while True:
      data_file = open("data.txt", "r+")
      data_file.seek(0)
      data_file.truncate()

      for i in data_list:
        data_file.writelines(i + "\n")

      data_file.close()
      
      
How to RECEIVE data from this microservice:

1. Make sure data-microservice.py, data.txt, results.txt and your program are in the same directory.
2. Have both programs running.
3. Include a segment of code in your program that opens the results.txt file and reads it.
4. Extract the calculated mean data how you prefer (i.e. if you just want the number implement code that reads only the 
numbers.
5. The first line of results.txt with contain "mean=SOMENUMBER" and the second line of results.txt will contain
"mode=SOMENUMBER,".
  Note: Mode may have multiple values separated by a comma.
