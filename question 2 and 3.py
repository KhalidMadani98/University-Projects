import os       #function for creating, removing and changing a directory.
import datetime #supplies classes to work with date and time


def printToFile(input):
    script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
    rel_path = "output.csv" #path of file. file is in python project folder. can be called upon directly.
    abs_file_path = os.path.join(script_dir, rel_path)

    with open(abs_file_path, "w") as f: #opening the file in write mode
        f.write("daily P&L,Date\n")     #writing to file
        for data in input:              #writing to each line following the subtraction of opening price and closing price.
            f.write(str(data[1] - data[0]) + "," + str(data[2]) + "\n") #calculation being carried out to calculate daily profit and loss


def readFile():
    #creating the input file path
    script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
    rel_path = "input.csv"                  #input file containing data prior to calculations
    abs_file_path = os.path.join(script_dir, rel_path)

    #variable to store input list
    input = []
    with open(abs_file_path, "r") as f:                   #opening the file in read mode
        for line in f.readlines()[1:]:                    #reading each line ignoring the header row
            line_items = line.split(",")                  #splitting each row into seperate variables with commas
            opening_price = float(line_items[0].strip())  #reading the opening price
            closing_price = float(line_items[1].strip())  #reading the closing price
            trade_date = datetime.datetime.strptime(line_items[2].strip(), '%d-%m-%Y') #reading date in dd-mm-yyyy format
            input.append((opening_price, closing_price, trade_date.date())) #appending each row to the input list

    printToFile(input)                                                      #calculating and printing the output

'''
This is the main function
'''
def main():
    readFile()


if __name__ == '__main__':
    main()
