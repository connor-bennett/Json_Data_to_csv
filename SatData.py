# Connor Bennett
# connbenn
# 4/ 24/ 22
# CS 162 Proj 5 pt c

# Write a class named SatData that reads a JSON file containing data on 2010 SAT results for New York City
# and writes the data to a text file in CSV format. That same JSON file will be provided as a local file in
# Gradescope named sat.json. Your code does not need to access the internet.

# CSV is a very simple format - just commas separating columns and newlines separating rows
# (see note below about commas that are part of field names). You'll see an example of CSV format below.
# There is a csv module for Python, but you will not use it for this project.
import json


class SatData:
    """
    Your class should have:
    an init method that reads the file and stores it in whatever data member(s) you prefer.
    Any data members of the SatData class must be private.
    """
    def __init__(self):

        with open('sat.json', 'r') as infile:
            self._data = json.load(infile)['data']

    def save_as_csv(self, dbns):
        """
        a method named save_as_csv that takes as a parameter a list of DBNs (district bureau numbers) and
        saves a CSV file that looks like this, but with only the rows that correspond to the DBNs in the list
        (and also the row of column headers). To see what CSV syntax looks like, open the file as a text file
        rather than as a spreadsheet. You may assume that all of the DBNs in the list passed to your method are
        present in the JSON file. The rows in the CSV file must be sorted in ascending order by DBN. The name
        of the output file must be output.csv.
        """
        header = "DBN,School Name,Number of Test Takers,Critical Reading Mean,Mathematics Mean,Writing Mean"
        information = []

        # loop to turn get desired json data and struture it to fit csv format
        for data in self._data:
            if data[8] in dbns:
                if "," in data[9]:
                    comma_stripped_or_not = '"' + data[9] + '"'
                else:
                    comma_stripped_or_not = data[9]

                schools_information = data[8] + "," + comma_stripped_or_not + "," + data[10] + "," + data[11] + "," + data[12] + "," + data[13], '\n'
                information.append(schools_information)

        information.sort()

        #write structure data from above to csv file
        with open('output.csv', 'w') as my_csv:
            my_csv.write(header)
            my_csv.write('\n')
            for item in information:
                string_tup = str(item)
                my_csv.write(string_tup)
                my_csv.write('\n')


def main():
    pass


if __name__ == '__main__':
    main()
