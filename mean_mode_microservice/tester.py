import time

data_list = ["15", "25", "80", "80", "20", "1", "1", "1", "24.5"]

while True:

    data_file = open("data.txt", "r+")
    data_file.seek(0)
    data_file.truncate()

    for i in data_list:
        data_file.writelines(i + "\n")

    data_file.close()

    time.sleep(15)