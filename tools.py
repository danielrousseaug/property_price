import enum
import geopy.distance
import csv
import numpy as np
"""
Test & Demo
"""
def main():

    # with open('properties.csv') as csv_file:
    #     csv_reader = csv.reader(csv_file, delimiter = ',')
    
    #     # list to store the names of columns
    #     lc = 0
    #     # loop to iterate through the rows of csv
    #     for row in csv_reader:
    #         lc+=1
    #         if lc < 4:
    #             for i, x in enumerate(row):
    #                 print(str(i) + ": " + str(x))

    # get property for testing
    with open('properties.csv') as csv_file:
        csv_reader = list(csv.reader(csv_file, delimiter=','))
        prop = csv_reader[4]

    # call the function and print the output
    info, dist = get_closest(prop)
    print("The closest property to \'" + prop[7] + "\' is:")
    print("-"*30)
    print("\'" + info[7] + "\'")
    print("Which is " + str(dist) + "km away\n\n")

    # call the function and print the output
    info, value = get_most_similair(prop)
    print("The most similair property to \'" + prop[7] + "\' is:")
    print("-"*30)
    print("\'" + info[7] + "\'")

    # call the function and print the output
    price = value_estimate(prop)
    print("\nThe estimated value of the property is:")
    print("-"*30)
    print(str(price) + str(prop[50]))


"""
get_closest(property):

Params
- property (list of characteristics as taken from row of property csv file)
Returns
- closest_property (the closest geographical property as a list of characteristics taken from property csv file)
- closest_distance (distance between the properties in km)
"""
def get_closest(property):
    # open coordinate csv file
    with open('with_coordinates.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        # init variables to store geographically closest property and its distance
        closest_property = []
        closest_distance = 999999.9

        # get coordinate pair of test property
        long = float(property[8])
        lat = float(property[9])
        coords_prop = (lat,long)

        # iterate through each row finding the closest one
        skip_headers = True
        for row in csv_reader:
            # skip header line
            if skip_headers:
                skip_headers = False
                continue
            
            # check if row has coordinates
            if not (row[8] == "N/A"):
                # set coordinates for current comparable property
                long = float(row[9])
                lat = float(row[8])
                coords_other = (lat,long)

                # get their distance
                distance = geopy.distance.geodesic(coords_other, coords_prop).km

                # compare distance, if their distance is smallest so far, set it as such
                if (distance < closest_distance):
                    closest_distance = distance
                    closest_property = row

        # return closest property and its distance in km to original property
        return closest_property, closest_distance

"""
get_most_similair(property):

Params
- property (list of characteristics as taken from row of property csv file)
Returns
- closest_property (the closest geographical property as a list of characteristics taken from property csv file)
- closest_distance (distance between the properties in km)
"""
def get_most_similair(property):
    # calculates similarity between two numbers
    def num_sim(n1, n2):
        return 1 - abs(n1 - n2) / (n1 + n2)

    # set array with columns for comparison
    comparable_columns = [8,9,41,42]

    # open coordinate csv file
    with open('with_coordinates.csv') as csv_file:
        # initialize most similair propety and its similarity value
        similair_prop = []
        similarity_value = 0

        # make bopl to skip headers and set csv interpreter
        csv_reader = csv.reader(csv_file, delimiter=',')
        skip_headers = True

        # iterate through each row finding the closest one
        for row in csv_reader:
            # skip header line
            if skip_headers:
                skip_headers = False
                continue
            
            # initialize similarity array 
            sim_arr = []

            # skip values with no coordinates
            if row[8] == "N/A":
                continue

            # get similarity for each column and add it to array
            for column in comparable_columns:
                column_similarity = num_sim(float(row[column].replace(',', '')),float(property[column].replace(',', '')))
                sim_arr.append(column_similarity)
            
            # add up array to get a similairty score
            sim_score = 0
            for value in sim_arr:
                sim_score += value

            # if score is bigger that previous max, set it as new most similair property
            if similarity_value < sim_score:
                similair_prop = row
                similarity_value = sim_score

        # return closest property and its distance in km to original property
        return similair_prop, similarity_value

"""
value_estimate(property):

Returns an estimate of a property's value based on
the most similair property, adjusting for square meters
"""
def value_estimate(property):
    # get the most similair property
    info, _ = get_most_similair(property)

    # get the value of the most similair property per meter squared
    # info [2] - price
    # info [16] - construction area
    m2_value = float(info[2])/float(info[42])

    # value estimate based on price of m2 multiplied by actual propertys m2
    estimate = m2_value * float(info[42])    
    
    return estimate


if __name__ == '__main__':
    main()