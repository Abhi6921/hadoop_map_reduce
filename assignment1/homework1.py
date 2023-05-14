import csv

def mapper(data_row):
    # extract the Nationality and player height and map then as key-value pairs
    nationality = data_row['Nationality']
    height = data_row['Height'].replace("'", ".")
    # return null if the empty cell in height column
    if height == '':
        return None
    return (nationality, (float(height), 1))

def reducer(heights):
    total_height = 0
    football_player_count = 0
    # iterate over the heights tuple and count the number of height value and add the height
    for height, count in heights:
        total_height += height
        football_player_count += count
    # find the average height and display the result.
    height_result = total_height / football_player_count
    rounded_height = round(height_result, 2)
    return (rounded_height)

#initialize the dictionary and append the output to it.
average_height_results = {}

#open and read the .csv file
with open('Soccer2019.csv', 'r') as csvFile:
    reader = csv.DictReader(csvFile)
    for row in reader:
        result = mapper(row)
        if result:
            # assign country and height_count from result unpacked from mapper function
            nationality, height_count = result
            # if country not in dict generate new key else append height
            if nationality not in average_height_results:
                average_height_results[nationality] = []
            average_height_results[nationality].append(height_count)

#iterate over the dictionary and display the results
for nationality, heights in average_height_results.items():
    average_height = reducer(heights)
    print(f"{nationality}: {average_height}")
